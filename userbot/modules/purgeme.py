import time
from userbot.events import register


@register(outgoing=True, pattern="^.purgeme")
async def purgeme(delme):
    """ For .purgeme, delete x count of your latest message."""
    if not delme.text[0].isalpha() and delme.text[0] not in ("/", "#", "@", "!"):
        message = delme.text
        count = int(message[9:])
        i = 1

        async for message in delme.client.iter_messages(delme.chat_id, from_user='me'):
            if i > count + 1:
                break
            i = i + 1
            await message.delete()

        smsg = await delme.client.send_message(
            delme.chat_id,
            "Ho eliminato i tuoi messaggi, messaggi eliminati: "
            + str(count),
        )
        time.sleep(1)
        i = 1
        await smsg.delete()