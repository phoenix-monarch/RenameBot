from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.progress import not_subscribed 
from config import FORCE_SUB
from Script import script

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢Join Update Channel📢", url=f"https://t.me/{FORCE_SUB}") ]]
    text = script.FSUB_MSG
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
