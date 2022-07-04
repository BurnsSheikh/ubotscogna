"""Emoji
Available Commands:
.fuck"""

from telethon import events
import asyncio
from userbot.events import register


@register(pattern="fuck")
@register(pattern=r"\.(.*)", outgoing=True)

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "fuck":

        await event.edit(input_str)

        animation_chars = [

            "🖕🏻🖕🏻🖕🏼🖕🏼🖕🏽🖕🏽🖕🏾🖕🏾🖕🏿",

            "🖕🏼🖕🏼🖕🏽🖕🏽🖕🏾🖕🏾🖕🏿🖕🏿🖕🏿"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 2])
