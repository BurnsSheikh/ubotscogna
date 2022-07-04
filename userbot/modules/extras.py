import asyncio, subprocess
import time, re, io, os
from collections import deque
from telethon import events, functions, types
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, CreateChannelRequest, DeleteMessagesRequest
from userbot.events import register

@register(outgoing=True, pattern="^.clock$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

