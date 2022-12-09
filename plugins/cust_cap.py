from pyrogram import Client, filters 
from helper.database import db
from Script import script

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text(script.GIV_CAP)
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text(script.SAV_CAP)

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text(script.EMPTY_CAP)
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text(script.DEL_CAP)
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ:-**\n\n`{caption}`")
    else:
       await message.reply_text(scrip.EMPTY_CAP)
