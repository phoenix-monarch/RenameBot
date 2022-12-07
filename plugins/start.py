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
            caption=script.START_TXT.format(message.from_user.first_name),
            reply_to_message_id = message.message_id,  
	    reply_markup=InlineKeyboardMarkup(
            [[ InlineKeyboardButton("DEVS ", callback_data='dev')                
                ],[
                InlineKeyboardButton('SUPPORT', url='https://t.me/Elsasupportgp'),
                InlineKeyboardButton('DONATE', callback='donate')
                ],[
                InlineKeyboardButton('ABOUT', callback_data='about'),
                InlineKeyboardButton('HELP', callback_data='help') ]  ]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=script.START_TXT.format(message.from_user.first_name),
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("DEVS ", callback_data='dev')                
                ],[
                InlineKeyboardButton('SUPPORT', url='https://t.me/Elsasupportgp'),
                InlineKeyboardButton('DONATE', callback='donate')
                ],[
                InlineKeyboardButton('ABOUT', callback_data='about'),
                InlineKeyboardButton('HELP', callback_data='help')
                ]]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=script.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("CLOSE", callback_data = "close"),
               InlineKeyboardButton("BACK", callback_data = "start")
               ]]
            )
        )
    elif data == "donate":
        await query.message.edit_text(
            text=script.DONATE_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("CLOSE", callback_data = "close"),
               InlineKeyboardButton("BACK", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=script.ABOUT_TXT, 
            reply_markup=InlineKeyboardMarkup([[           
               InlineKeyboardButton("CLOSE", callback_data = "close"),
               InlineKeyboardButton("BACK", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=script.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[               
               InlineKeyboardButton("CLOSE", callback_data = "close"),
               InlineKeyboardButton("BACK", callback_data = "start")
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
       f"""__𝘞𝘩𝘢𝘵 𝘋𝘰 𝘠𝘰𝘶 𝘞𝘢𝘯𝘵 𝘔𝘦 𝘛𝘰 𝘋𝘰 𝘞𝘪𝘵𝘩 𝘛𝘩𝘪𝘴 𝘍𝘪𝘭𝘦?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Rename 📝",callback_data = "rename")
       ,InlineKeyboardButton("Cancel ❌",callback_data = "cancel")  ]]))
