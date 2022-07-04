import asyncio
from userbot.events import register
from asyncio import sleep
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from userbot import HELPER
from userbot.events import register
from telethon.utils import get_input_location
import random

@register(outgoing=True, pattern=".previsione ?(.*)")
async def _(target):
    message = await target.get_reply_message()
    if target.fwd_from:
        return
    r = random.randint(1, 100)
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
    testo = f'''**🔮 Previsione del futuro **

{name} pensa ad una domanda e io ti risponderò con "Sì" o "No".'''
    attendi = '__🔮 Previsione in corso... 🔮__'
    input_str = target.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "testa":
            await target.edit(testo)
            await asyncio.sleep(3)
            await target.edit(attendi)
            await asyncio.sleep(1)
            await target.edit("""**✅ Previsione effettuata 🔮**

❓La risposta alla domanda posta è **Si**!""")
        elif input_str == "croce":
            await target.edit(testo)
            await asyncio.sleep(3)
            await target.edit(attendi)
            await asyncio.sleep(1)
            await target.edit("""**✅ Previsione effettuata 🔮**

❓La risposta alla domanda posta è **No!**!""")
        else:
            await target.edit(testo)
            await asyncio.sleep(3)
            await target.edit(attendi)
            await asyncio.sleep(1)
            await target.edit("""**✅ Previsione effettuata 🔮**

❓La risposta alla domanda posta è **Si**!""")
    elif r % 2 == 0:
        if input_str == "croce":
            await target.edit(testo)
            await asyncio.sleep(3)
            await target.edit(attendi)
            await asyncio.sleep(1)
            await target.edit("""**✅ Previsione effettuata 🔮**

❓La risposta alla domanda posta è **No!**!""")
        elif input_str == "testa":
            await target.edit(testo)
            await asyncio.sleep(3)
            await target.edit(attendi)
            await asyncio.sleep(1)
            await target.edit("""**✅ Previsione effettuata 🔮**

❓La risposta alla domanda posta è **Si**!""")
        else:
            await target.edit(testo)
            await asyncio.sleep(3)
            await target.edit(attendi)
            await asyncio.sleep(1)
            await target.edit("""**✅ Previsione effettuata 🔮**

❓La risposta alla domanda posta è **No!**""")
    else:
        await target.edit("¯\_(ツ)_/¯")


random_number = random.randint(0, 100)
random_num = random.randint(0, 100)

@register(outgoing=True, pattern="^.fortuna$")
async def fortuna(target):
    message = await target.get_reply_message()
    random_number = random.randint(0, 100)
    random_num = random.randint(0, 100)
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(f"""**☘️ Calcolo della fortuna**

{name} __sei fortunato o sfortunato!?__
__🦦 Scopriamolo 😄__""")
        await asyncio.sleep(3.0)
        await target.edit(f"""__🔄 Calcolo in corso...__""")
        await asyncio.sleep(2.0)
        await target.edit(f"""**✅ Calcolo fortuna effettuato**

☘️ {name} sei fortunato al {random_number}%.

👎🏻 {name} sei sfortunato al {random_num}%""")
    else:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")

@register(outgoing=True, pattern="^.win$")
async def win(target):
    await target.edit(f"""🚦🚘🚘🚘 3⃣""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚦🚘🚘🚘 2⃣""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚦🚘🚘🚘 1⃣""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚦🚘🚘🚘 🏁""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚩                 🚗💨""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚩     🚗💨""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚩 🚗💨""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🥇🏆 🚘 🏆🥇""")



@register(outgoing=True, pattern="^.aereo$")
async def win(target):
    await target.edit(f"""🛩

        🏢""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🛩
        🏢""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🔥
🔥🏢🔥
     🔥""")
    await asyncio.sleep(1.0)
    await target.edit(f"""💥
💥🏢💥
     💥""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🔥🔥🔥""")

@register(outgoing=True, pattern="^.light$")
async def light(target):
    message = await target.get_reply_message()
    random_number = random.randint(0, 456)
    random_num = random.randint(0, 456)
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(f"""**✔️ Game Started** 🛗""")
        await asyncio.sleep(2.0)
        await target.edit(f"""👧🏻 : 
__🟢 Green Light...__""")
        await asyncio.sleep(3.0)
        await target.edit(f"""👧🏻 : 
**🔴 Red Light!!**""")
        await asyncio.sleep(3.0)
        await target.edit(f"""👀 🤖""")
        await asyncio.sleep(2.0)
        await target.edit(f"""🏃🏻💥🔫""")
        await asyncio.sleep(3.0)
        await target.edit(f"""__Player {name} [{random_number}] eliminated.__""")
    else:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")


@register(outgoing=True, pattern="^.circo$")
async def circo(target):
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(f"""**🤹🏻‍♂️ Er circo generator!**

🎙 A breve estrarrò **un utente** da questo gruppo, **la persona estratta** sarà definita **"clown del gruppo"**.""")
        await asyncio.sleep(2.0)
        await target.edit(f"""__📤 Sto estraendo la persona...__""")
        await asyncio.sleep(2.0)
        await target.edit(f"""**🤹🏻‍♂️ Er circo generator!**

**🎉 Complimenti** {name}, sei il nuovo **clown** del gruppo 🤡

__🎪 Forza sbrigati!! Il circo ti sta aspettando.__""")
    else:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")

@register(outgoing=True, pattern="^.sun$")
async def sun(target):
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(f"""☀️ ☁️ 

__💁🏻 "che bella giornata oggi!"__.""")
        await asyncio.sleep(2.0)
        await target.edit(f"""* Arriva {name} *""")
        await asyncio.sleep(2.0)
        await target.edit(f"""⛈🌪💨

🙎🏻 "ma procodd**""")
    else:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")


@register(outgoing=True, pattern="^.diritti$")
async def diritti(target):
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(f"""**📇 Calcolo dei diritti**

__{name} a breve calcolerò quanti diritti hai!__""")
        await asyncio.sleep(2.0)
        await target.edit(f"""__🗳 Inizio il calcolo...__""")
        await asyncio.sleep(2.0)
        await target.edit(f"""**📈 Calcolo dei diritti terminato**

⚠️❗️⚠️❗️⚠️❗️⚠️❗️⚠️❗️⚠️❗️""")
        await asyncio.sleep(2.0)
        await target.edit(f"""**📈 Calcolo dei diritti terminato**

**__⚠️❗️ Errore nel sistema ❗️⚠️__**

📛 {name} è un utente **senza alcun diritto!**
__👩🏻 Probabilmente è una donna__""")
    else:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")


@register(outgoing=True, pattern="^.prelievo$")
async def prelievo(target):
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(f"""**🧪 Test iniziato!**

Oggi controlliamo l'organismo di {name}.""")
        await asyncio.sleep(2.0)
        await target.edit(f"""__🩸Prelevo un campione di sangue da {name}.__""")
        await asyncio.sleep(3.0)
        await target.edit(f"""**✅ Fatto!** {name} spero tu non abbia sentito troppo dolore 😇""")
        await asyncio.sleep(2.0)
        await target.edit(f"""__💉 Mando il campione in laboratorio per un'analisi.__""")
        await asyncio.sleep(2.0)
        await target.edit(f"""
        **🧪 Analisi effettuata!**

😨 {name} sei risultato positivo all'**epatite** di tipo C...

😰 Siamo tutti con te.🥺""")
    else:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")

random_number = random.randint(0, 100)

@register(outgoing=True, pattern="^.gaytest$")
async def prelievo(target):
    message = await target.get_reply_message()
    random_number = random.randint(0, 100)
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(f"""**🏳‍🌈 Quanto sei gay Test**

Ciao a tutti, oggi analizziamo la percentuale gay di {name}.""")
        await asyncio.sleep(3.0)
        await target.edit(f"""**🧬 Risultati ottenuti!**

✅ {name} è risultato **positivo gay** al {random_number}%.

__👥 Consiglio di allontanarsi, potrebbe essere contagioso...__""")
    else:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")


a = """||            🚙"""
b = """||         🚙"""
c = """**Una piotta e dieci così, terza marcia, terza marcia, terza marcia.**"""
d = """__NON CI SONO PROBLEMI, NON CI SONO PROBLEMI__"""
e = """__Vi insegno a guidare...__"""
f = """||     🚙"""
g = """||  🚙"""
h = """**🚦 QUANDO IL SEMAFORO È ROSSO 🟢**"""
i = """🚦 QUANDO IL SEMAFORO È ROSSO 🟠"""
j = """🚦 QUANDO IL SEMAFORO È ROSSO 🔴"""
k = """**🚦 QUANDO IL SEMAFORO È ROSSO 🟢**"""
l = """**Si fa così, si fa così: taac.**"""
m = """Je imbocchi qua, je rigiri qua, fratellì, così."""
n = """|| 🚙"""
o = """||🚙"""
p = """Bada fratellì, **ho sfondato tutto fratellì**, ho sfonnato tutto."""
q = """__Ho preso er muro fratellì, te dico fermati fratellì. Ho preso er muro. ♿️__"""



@register(outgoing=True, pattern="^.muro$")
async def muro(target):
    global tempo
    await target.edit(a)
    await asyncio.sleep(1.0)
    await target.edit(b)
    await asyncio.sleep(1.0)
    await target.edit(c)
    await asyncio.sleep(2.0)
    await target.edit(d)
    await asyncio.sleep(2.0)
    await target.edit(e)
    await asyncio.sleep(2.0)
    await target.edit(f)
    await asyncio.sleep(2.0)
    await target.edit(g)
    await asyncio.sleep(2.0)
    await target.edit(h)
    await asyncio.sleep(2.0)
    await target.edit(i)
    await asyncio.sleep(2.0)
    await target.edit(j)
    await asyncio.sleep(2.0)
    await target.edit(k)
    await asyncio.sleep(2.0)
    await target.edit(l)
    await asyncio.sleep(2.0)
    await target.edit(m)
    await asyncio.sleep(2.0)
    await target.edit(n)
    await asyncio.sleep(2.0)
    await target.edit(o)
    await asyncio.sleep(2.0)
    await target.edit(p)
    await asyncio.sleep(2.0)
    await target.edit(q)
    await asyncio.sleep(2.0)