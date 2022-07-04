from userbot.events import register

@register(outgoing=True, pattern="^.chatid$")
async def chatidgetter(chat):
    """ For .chatid, returns the ID of the chat you are in at that moment. """
    if not chat.text[0].isalpha() and chat.text[0] not in ("/", "#", "@", "!"):
        await chat.edit("Chat ID: `" + str(chat.chat_id) + "`")