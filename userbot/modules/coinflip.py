from telethon import events
import random, re
import asyncio
from userbot.events import register


@register(outgoing=True, pattern=".moneta ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "testa":
            await event.edit("🪙 Lancio una moneta...")
            await asyncio.sleep(1)
            await event.edit("✅ La moneta è atterrata! È uscito testa.")
        elif input_str == "croce":
            await event.edit("🪙 Lancio una moneta...")
            await asyncio.sleep(1)
            await event.edit("✅ La moneta è atterrata! È uscito croce, hai perso")
        else:
            await event.edit("🪙 Lancio una moneta...")
            await asyncio.sleep(1)
            await event.edit("✅ La moneta è atterrata! È uscito testa.")
    elif r % 2 == 0:
        if input_str == "croce":
            await event.edit("🪙 Lancio una moneta...")
            await asyncio.sleep(1)
            await event.edit("✅ La moneta è atterrata! È uscito croce, hai vinto")
        elif input_str == "testa":
            await event.edit("🪙 Lancio una moneta...")
            await asyncio.sleep(1)
            await event.edit("✅ La moneta è atterrata! È uscito testa, hai perso")
        else:
            await event.edit("🪙 Lancio una moneta...")
            await asyncio.sleep(1)
            await event.edit("✅ La moneta è atterrata! È uscito croce.")
    else:
        await event.edit("¯\_(ツ)_/¯")