from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from Script import script
from helper.database import db
from config import START_PIC, FLOOD, ADMIN 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    await message.reply_photo(
            photo=START_PIC,
            caption=script.START_TXT.format(message.from_user.mention),
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
            text=script.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[    
               InlineKeyboardButton("〄 sᴏᴜʀᴄᴇ 〄", url="https://github.com/Devil-Botz/RenameBot") ],[      
               InlineKeyboardButton("🗑️ᴄʟᴏsᴇ🗑️", callback_data = "close"),
               InlineKeyboardButton("⌫ʙᴀᴄᴋ☽", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=script.DEV_TXT,
            reply_markup=InlineKeyboardMarkup([[
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


@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**Wʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ.?**\n\n**Fɪʟᴇ Nᴀᴍᴇ** :- `{filename}`\n\n**Fɪʟᴇ Sɪᴢᴇ** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("✅ ʀᴇɴᴀᴍᴇ ✅", callback_data="rename") ],
                   [ InlineKeyboardButton("❌ ᴄᴀɴᴄᴇʟ ❌", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**Wʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ.?__**\n\n**Fɪʟᴇ Nᴀᴍᴇ* :- `{filename}`\n\n**Fɪʟᴇ Sɪᴢᴇ** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("✅ ʀᴇɴᴀᴍᴇ ✅", callback_data="rename") ],
                   [ InlineKeyboardButton("❌ ᴄᴀɴᴄᴇʟ ❌", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass
