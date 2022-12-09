from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
       new_name = message.text 
       await message.delete() 
       msg = await client.get_messages(message.chat.id, reply_message.id)
       file = msg.reply_to_message
       media = getattr(file, file.media.value)
       if not "." in new_name:
          if "." in media.file_name:
              extn = media.file_name.rsplit('.', 1)[-1]
          else:
              extn = "mkv"
          new_name = new_name + "." + extn
       await reply_message.delete()

       button = [[InlineKeyboardButton("📂 ᴅocuments",callback_data = "upload_document")]]
       if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
           button.append([InlineKeyboardButton("🎥 ᴠɪᴅᴇᴏ",callback_data = "upload_video")])
       elif file.media == MessageMediaType.AUDIO:
           button.append([InlineKeyboardButton("🎵 ᴀᴜᴅɪᴏ",callback_data = "upload_audio")])
       await message.reply_text(
          Sᴇʟᴇᴄᴛ ᴛʜᴇ ᴏᴜᴛᴘᴜᴛ ғɪʟᴇ ᴛʏᴘᴇ**\n**• Fɪʟᴇ Nᴀᴍᴇ :-**```{new_name}```",
          reply_to_message_id=file.id,
          reply_markup=InlineKeyboardMarkup(button))
