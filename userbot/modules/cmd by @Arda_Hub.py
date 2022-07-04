############################################################
#cmds by @Arda_Hub
############################################################

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register
from userbot import bot
from time import sleep

@register(outgoing=True, pattern="^.sg(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Rispondi al messaggio di un utente")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("Rispondi al messaggio di un utente")
       return
    chat = "@SangMataInfo_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("Rispondi al messaggio di un utente, non di un bot!")
       return
    await event.edit("Sto cercando...")
    async with bot.conversation(chat, exclusive=False) as conv:
          response = None
          try:
              msg = await reply_message.forward_to(chat)
              response = await conv.get_response(message=msg, timeout=5)
          except YouBlockedUserError: 
              await event.edit(f"Sblocca {chat} e riprova")
              return
          except Exception as e:
              print(e.__class__)

          if not response:
              await event.edit("Bot probabilmente offline")
          elif response.text.startswith("Forward"):
             await event.edit("Errore, le impostazioni privacy dell'utente non permettono di visualizzare la sua cronologia nomi/username")
          else: 
             await event.edit(response.text)
          sleep(1)
          await bot.send_read_acknowledge(chat, max_id=(response.id+3))
          await conv.cancel_all()

############################################################

from asyncio import sleep
from userbot.events import register

@register(outgoing=True, pattern=r"\.kickme$")
async def kickme(leave):
    """Comando per autokickarti by @Arda_Hub"""
    await leave.edit("Ciao ciao👋")
    await leave.client.kick_participant(leave.chat_id, 'me')

############################################################

from telethon.tl.types import ChannelParticipantsAdmins
from userbot.events import register

@register(outgoing=True, pattern="all( (.*)|$)")
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    mentions = input_str or "@all"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100):
        mentions += f"[............all............](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()