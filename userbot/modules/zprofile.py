import os

from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError

from telethon.errors.rpcerrorlist import (PhotoExtInvalidError,
                                          UsernameOccupiedError)

from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest

from telethon.tl.functions.photos import (DeletePhotosRequest,
                                          GetUserPhotosRequest,
                                          UploadProfilePhotoRequest)

from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel

from userbot import bot
from userbot.events import register

# ====================== CONSTANT ===============================
INVALID_MEDIA = "```Media invalido.```"
PP_CHANGED = "```Immagine di profilo cambiata con successo```"
PP_TOO_SMOL = "```L'immagine è di una risoluzione troppo bassa.```"
PP_ERROR = "```Si è verificato un errore durante l'elaborazione dell'immagine.```"

BIO_SUCCESS = "```Bio editata con successo.```"

USERNAME_SUCCESS = "```Username editato con successo.```"
USERNAME_TAKEN = "```Questo username è occupato ;(.```"
# ===============================================================


@register(outgoing=True, pattern="^\.riservati$")
async def mine(event):
    """ Con il comando .riservati, ottieni un elenco dei tuoi nomi utente riservati.. """
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.edit(output_str)


@register(outgoing=True, pattern="^\.name")
async def update_name(name):
    """ Cambia il nome telegram. """
    newname = name.text[6:]
    if " " not in newname:
        firstname = newname
        lastname = ""
    else:
        namesplit = newname.split(" ", 1)
        firstname = namesplit[0]
        lastname = namesplit[1]

    await name.client(
        UpdateProfileRequest(first_name=firstname, last_name=lastname))
    await name.edit(f"""✅ Nome modificato con successo.

💬 Nome attuale:
{firstname}{lastname}""")


@register(outgoing=True, pattern="^\.setpfp$")
async def set_profilepic(propic):
    """ Imposta l'immagine di profilo . """
    replymsg = await propic.get_reply_message()
    photo = None
    if replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await propic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await propic.client.download_file(replymsg.media.document)
        else:
            await propic.edit(INVALID_MEDIA)

    if photo:
        try:
            await propic.client(
                UploadProfilePhotoRequest(await
                                          propic.client.upload_file(photo)))
            os.remove(photo)
            await propic.edit(PP_CHANGED)
        except PhotoCropSizeSmallError:
            await propic.edit(PP_TOO_SMOL)
        except ImageProcessFailedError:
            await propic.edit(PP_ERROR)
        except PhotoExtInvalidError:
            await propic.edit(INVALID_MEDIA)


@register(outgoing=True, pattern="^\.cb (.*)")
async def set_biograph(setbio):
    """ Imposta la bio. """
    newbio = setbio.pattern_match.group(1)
    await setbio.client(UpdateProfileRequest(about=newbio))
    await setbio.edit(f"""✅ Biografia modificata con successo.

💬 Biografia attuale:
{newbio}""")


@register(outgoing=True, pattern="^\.username (.*)")
async def update_username(username):
    """ Modifica l'username. """
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await username.edit(USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await username.edit(USERNAME_TAKEN)

@register(outgoing=True, pattern=r"^\.delpfp")
async def remove_profilepic(delpfp):
    """ Rimuove una foto profila. """
    group = delpfp.text[8:]
    if group == 'all':
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1

    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.from_id,
                             offset=0,
                             max_id=0,
                             limit=lim))
    input_photos = []
    for sep in pfplist.photos:
        input_photos.append(
            InputPhoto(id=sep.id,
                       access_hash=sep.access_hash,
                       file_reference=sep.file_reference))
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(
        f"`Foto eliminata con successo {len(input_photos)}`")
