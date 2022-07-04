import asyncio
from asyncio import sleep
from userbot.events import register

from collections import deque


@register(outgoing=True, pattern="^.moon")
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
	    if event.fwd_from:
		    return
	    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	    for _ in range(32):
		    await asyncio.sleep(0.1)
		    await event.edit("".join(deq))
		    deq.rotate(1)

@register(outgoing=True, pattern="^.rrr$")
async def rrr(e):
    if e.fwd_from:
        return
    usr = await e.get_sender()
    if usr.last_name == None:
      USER = usr.first_name
    else:
      USER = usr.first_name + " " + usr.last_name
      await e.edit(f"{USER}")



      



import io
import traceback
from datetime import datetime
from selenium import webdriver
from telethon import events
from userbot import bot

@register(outgoing=True, pattern="^.test$")
async def _(e):
  await e.edit("**✅ Userbot online!**")

@register(outgoing=True, pattern=f"[.]hack")
async def hack(e):
    if e.fwd_from:
        return
    usr = await e.get_sender()
    if usr.last_name == None:
      USER = usr.first_name
    else:
      USER = usr.first_name + " " + usr.last_name
    animation_interval = 2
    animation_ttl = range(0, 12)
    #input_str = event.pattern_match.group(1)
    #if input_str == "hack":
    await e.edit("Inizio Hacking")
    animation_chars = [

            "Connessione a Telegram Data Center",
            f"Target Selected By Hacker » {USER}",
            "Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
            "**Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package",
            "**Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)",
            "**Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'",
            "**Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e",
            "**Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b",
            "**Hacking... 84%\n█████████████████████▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database",
            "Hacking... 100%\n█████████HACKED███████████ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**\n\n\n🔹Output: Generating.....",
            f"**Account Hackerato..."
        ]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await e.edit(animation_chars[i % 12])

@register(pattern="[.]pene", outgoing=True)
async def pene(e):
    inizio = "............ ▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n"
    fine = "....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀ ▀▀▀▀▀\n"
    mezzoo = "....▐░░░░░░░░░░░▌\n"
    mezzo = ""
    for x in range(10):
        mezzo = mezzo + mezzoo
        await asyncio.wait([e.edit(inizio+mezzo+fine)])
        await asyncio.sleep(0.3)