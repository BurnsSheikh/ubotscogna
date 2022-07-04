""" Userbot module for getiing info about any user on Telegram(including you!). """

import os

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from userbot import HELPER
from userbot.events import register
from telethon.utils import get_input_location


TMP_DOWNLOAD_DIRECTORY = "./"


@register(pattern=".info(?: |$)(.*)", outgoing=True)
async def who(event):
    """ For .whois command, get info about a user. """
    if event.fwd_from:
        return

    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)

    replied_user = await get_user(event)

    photo, caption = await fetch_info(replied_user, event)

    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html"
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await event.delete()

    except TypeError:
        await event.edit(caption, parse_mode="html")
    except:
        await event.edit("__⚠️ » Inserisci un ID o Username valido.__")


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
            await event.edit("__⚠️ » Inserisci un ID o Username valido.__")
            return None
        except:
            await event.edit("__⚠️ » Inserisci un ID o Username valido.__")

    return replied_user

async def fetch_info(replied_user, event):
    """ Get details from the User object. """
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id,
        TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True
    )
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        dc_id = "✖️"
    if first_name:
        first_name = first_name.replace("\u2060", "")
    else:
        first_name = "✖️"
    if last_name:
        last_name = last_name.replace("\u2060", "")
    else:
        last_name = "✖️"
    if username:
        username = format(username)
    else:
        username = "✖️"
    if user_bio:
        user_bio = user_bio
    else:
        user_bio = "✖️."
    if replied_user.user.bot:
        is_bot = "✅"
    else:
        is_bot = "✖️"
    if replied_user.user.verified:
        verified = "✅"
    else:
        verified = "✖️"

    caption = "<b>ℹ️ INFO UTENTE ℹ️</b> \n\n"
    caption += f"• <b>🧑🏻Nome:</b> {first_name} \n"
    caption += f"• <b>🔖Cognome:</b> {last_name} \n"
    caption += f"• <b>🌐Username:</b> @{username} \n"
    caption += f"• <b>🤖Bot:</b> {is_bot} \n"
    caption += f"• <b>🆔ID:</b> <code>{user_id}</code> \n"
    caption += f"• <b>📡DC:</b> {dc_id}\n"
    caption += f"• <b>💬Chat in comune:</b> {common_chat} \n"
    caption += f"• <b>📖Bio:</b> <code>{user_bio}</code> \n\n"
    caption += f"• <b>🔗Permalink:</b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'

    return photo, caption