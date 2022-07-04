from telethon.tl.types import ChannelParticipantsAdmins
from userbot.events import register

@register(outgoing=True, pattern=".tagall")
async def fgdgd(event):
    if event.fwd_from:
        return
    mentions = """
.-..-.
`·.·´
●/
/▌
/ \ 
"""
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()