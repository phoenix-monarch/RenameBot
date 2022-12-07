from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply,CallbackQuery)
import humanize
import os
from helper.database import  insert 
from Script import script
START_PIC = os.environ.get("START_PIC", "")

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_photo(
            photo=START_PIC,
            caption=script.START_TXT.format(message.from_user.mention),
            reply_to_message_id = message.message_id,  
	    reply_markup=InlineKeyboardMarkup(
            [[ InlineKeyboardButton("⚔ ᴅᴇᴠs ⚔", callback_data='dev')                
                ],[
                InlineKeyboardButton('〄 sᴜᴘᴘᴏʀᴛ 〄', url='https://t.me/Elsasupportgp'),
                InlineKeyboardButton('〄 ᴅᴏɴᴀᴛᴇ 〄', callback_data='donate')
                ],[
                InlineKeyboardButton('〄 ᴀʙᴏᴜᴛ 〄', callback_data='about'),
                InlineKeyboardButton('〄 ʜᴇʟᴘ 〄', callback_data='help') ]  ]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("⚔ ᴅᴇᴠs ⚔", callback_data='dev')                
                ],[
                InlineKeyboardButton('〄 sᴜᴘᴘᴏʀᴛ 〄', url='https://t.me/Elsasupportgp'),
                InlineKeyboardButton('〄 ᴅᴏɴᴀᴛᴇ 〄', callback_data='donate')
                ],[
                InlineKeyboardButton('〄 ᴀʙᴏᴜᴛ 〄', callback_data='about'),
                InlineKeyboardButton('〄 ʜᴇʟᴘ 〄', callback_data='help')
                ]]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=script.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🗑️ᴄʟᴏsᴇ🗑️", callback_data = "close"),
               InlineKeyboardButton("⌫ʙᴀᴄᴋ☽", callback_data = "start")
               ]]
            )
        )
    elif data == "donate":
        await query.message.edit_text(
            text=script.DONATE_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🗑️ᴄʟᴏsᴇ🗑️", callback_data = "close"),
               InlineKeyboardButton("⌫ʙᴀᴄᴋ☽", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([[           
               InlineKeyboardButton("🗑️ᴄʟᴏsᴇ🗑️", callback_data = "close"),
               InlineKeyboardButton("⌫ʙᴀᴄᴋ☽", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=script.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[               
               InlineKeyboardButton("🗑️ᴄʟᴏsᴇ🗑️", callback_data = "close"),
               InlineKeyboardButton("⌫ʙᴀᴄᴋ☽", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()


@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__Wʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ.?__\n\n**Fɪʟᴇ Nᴀᴍᴇ** :- `{filename}`\n\n**Fɪʟᴇ Sɪᴢᴇ** :- `{filesize}`"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("✅ ʀᴇɴᴀᴍᴇ ✅",callback_data = "rename")
       ,InlineKeyboardButton("❌ ᴄᴀɴᴄᴇʟ ❌",callback_data = "cancel")  ]]))
