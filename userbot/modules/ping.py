import datetime

from userbot.events import register


@register(outgoing=True, pattern="^.ping$")
async def ping(event):
    now = datetime.datetime.now()
    await event.edit('Pinging...')
    later = datetime.datetime.now()
    delta = later - now
    await event.edit('Pong!\n' + str(int(delta.total_seconds() * 1000)) + 'ms' )