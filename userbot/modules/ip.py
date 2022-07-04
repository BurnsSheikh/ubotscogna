import json
import urllib.request

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register

@register(outgoing=True, pattern=".ip (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    adress = input_str

    token = "19e7f2b6fe27deb566140aae134dec6b"

    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1"

    result = urllib.request.urlopen(api).read()
    result = result.decode()

    result = json.loads(result)
    a = result["type"]
    b = result["country_code"]
    c = result["region_name"]
    d = result["city"]
    e = result["zip"]
    f = result["latitude"]
    g = result["longitude"]
    await event.edit(
        f"<b><u>ℹ️Informazioni raccolte</b></u>\n\n<b>Tipo : </b><code>{a}</code>\n<b>Nazione: </b> <code>{b}</code>\n<b>Stato/Regione : </b><code>{c}</code>\n<b>Citta : </b><code>{d}</code>\n<b>CAP : </b><code>{e}</code>\n<b>Latidutine : </b> <code>{f}</code>\n<b>Longitudine : </b><code>{g}</code>\n",
        parse_mode="HTML",
    )