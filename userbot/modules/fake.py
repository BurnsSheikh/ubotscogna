from userbot.events import register
from time import sleep
import asyncio


@register(outgoing=True, pattern="^.fmess(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Errore di sintassi`")
    await event.edit(f"✅ Ok")
    await asyncio.sleep(0.5)
    await event.delete()
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Errore di sintassi`")
    await event.edit(f"✅ Ok")
    await asyncio.sleep(0.5)
    await event.delete()
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Errore di sintassi`")
    await event.edit(f"✅ Ok")
    await asyncio.sleep(0.5)
    await event.delete()
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgioco(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Errore di sintassi`")
    await event.edit(f"✅ Ok")
    await asyncio.sleep(0.5)
    await event.delete()
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)