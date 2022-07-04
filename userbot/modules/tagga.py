from bs4 import BeautifulSoup
from requests import get
from userbot.events import register
from telethon.tl.types import DocumentAttributeAudio
from datetime import datetime
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName



async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return replied_user

@register(outgoing=True, pattern="^.tagga (.*)")
async def _(event):
	if event.fwd_from:
		return	
	replied_user = await get_user(event)
	input_str = event.pattern_match.group(1)
	user_id = replied_user.user.id
	if event.reply_to_msg_id:
		previous_message = await event.get_reply_message()
		if previous_message.forward:
			replied_user = previous_message.forward.from_id
		else:
			replied_user = previous_message.from_id
	else:
		await event.edit("Rispondi ad un messaggio")
	caption = """<a href='tg://user?id={}'>{}</a>""".format(user_id, input_str)
	await event.edit(caption, parse_mode="HTML")



