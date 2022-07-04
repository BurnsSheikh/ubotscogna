from telethon.tl import functions
from telethon import events, types
import asyncio

from asyncio import sleep
from os import remove
from telethon import events
from telethon.tl import functions, types
from platform import python_version, uname
from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (PeerChannel, ChannelParticipantsAdmins,
                               ChatAdminRights, ChatBannedRights,
                               MessageEntityMentionName, MessageMediaPhoto,
                               ChannelParticipantsBots)

from userbot import bot
from userbot.events import register


@register(outgoing=True, pattern=r"\.create (s|g|c)(?: |$)(.*)")
async def telegraphs(grop):
    """Utilizza .create per creare un gruppo o canale"""
    if grop.text[0].isalpha() or grop.text[0] in ("/", "#", "@", "!"):
        return
    if grop.fwd_from:
        return
    type_of_group = grop.pattern_match.group(1)
    group_name = grop.pattern_match.group(2)
    if type_of_group == "s":
        try:
            result = await grop.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                users=["@GroupHelpBot"],
                # Not enough users (to create a chat, for example)
                # Telegram, no longer allows creating a chat with ourselves
                title=group_name
            ))
            created_chat_id = result.chats[0].id
            result = await grop.client(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await grop.edit("Il gruppo {0} è stato creato. Premi [{0}]({1}) per entrare".format(group_name, result.link))
        except Exception as e:  # pylint:disable=C0103,W0703
            await grop.edit(str(e))
    elif type_of_group in ("g", "c"):
        try:
            r = await grop.client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                title=group_name,
                about="Welcome",
                megagroup=not bool(type_of_group == "c")
            ))
            created_chat_id = r.chats[0].id
            result = await grop.client(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await grop.edit("Il tuo gruppo/canale {0} è stato creato. Premi [{0}]({1}) per entrare".format(group_name, result.link))
        except Exception as e:  # pylint:disable=C0103,W0703
            await grop.edit(str(e))




#@borg.on(events.NewMessage(pattern=r"\-listmyusernames", outgoing=True))
#async def _(event):
@register(outgoing=True, pattern="^.usernameoccupati$")
async def usernames(event):
    if event.fwd_from:
        return
    result = await bot(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"» {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)
    
#@borg.on(events.NewMessage(pattern=r"\-listmychatids", outgoing=True))
#async def _(event):
@register(outgoing=True, pattern=".chatidoccupati$")
async def userid(event):
    if event.fwd_from:
        return
    result = await bot(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"» -{channel_obj.id} \n"
    await event.edit(output_str)