
from telethon import events
import os
import requests
import json
import asyncio, subprocess

import datetime
from telethon import functions
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from collections import deque

from telethon import events
import wikipedia
from userbot.events import register


@register(outgoing=True, pattern=".search (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.edit("__🔎 Sto cercando {} su wikipedia...__".format(input_str))
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"• [{s}]({url}) \n"
    await event.edit("✅ Ho cercato {} su wikipedia!\n\n🔗 Risultati della ricerca:\n\n{}".format(input_str, result))

@register(outgoing=True, pattern="^.heart$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("❤️🧡💛💚💙💜🖤"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)

@register(outgoing=True, pattern="^.medio$")
async def _(event):
    if event.fwd_from:
        return
    help_string = """
......................................../´¯/) 
......................................,/¯../ 
...................................../..../ 
..................................../´.¯/
..................................../´¯/
..................................,/¯../ 
................................../..../ 
................................./´¯./
................................/´¯./
..............................,/¯../ 
............................./..../ 
............................/´¯/
........................../´¯./
........................,/¯../ 
......................./..../ 
....................../´¯/
....................,/¯../ 
.................../..../ 
............./´¯/'...'/´¯¯`·¸ 
........../'/.../..../......./¨¯\ 
........('(...´...´.... ¯~/'...') 
.........\.................'...../ 
..........''...\.......... _.·´ 
............\..............( 
..............\.............\...
    """
    await event.edit(help_string)



@register(outgoing=True, pattern=".url (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("**✅ Link nascosto creato!**\n\n🔗 Link originale: {} \n\n🤫 Link nascosto: {}.".format(input_str, response_api))
    else:
        await event.edit("__❌ Errore!__")


@register(outgoing=True, pattern=".unshort (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith('3'):
        await event.edit("**✅ Riscontro ottenuto!**\n\n🔐 {} risulta essere un link nascosto.\n\n🔗 Link originale: {}".format(input_str, r.headers["Location"]))
    else:
        await event.edit("**❌ Nessun riscontro ottenuto!**\n\n🔐 {} non è un link nascosto.".format(input_str))