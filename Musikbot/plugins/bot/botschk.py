import random
from pyrogram import filters
from Musikbot import app
from Musikbot import *
from ... import *
import config

from ...logging import LOGGER

from Musikbot import app, userbot
from Musikbot.core.userbot import *

import asyncio

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from dotenv import load_dotenv
from Musikbot.core.userbot import Userbot
from datetime import datetime

# Assuming Userbot is defined elsewhere
userbot = Userbot()


BOT_LIST = ["Joox Music", "String Sessions1", "String Sessions2"]

@app.on_message(filters.command("cekbot") & filters.user(OWNER_ID))
async def bots_chk(_, message):
    msg = await message.reply_photo(photo="https://mallucampaign.in/images/img_1709026510.jpg", caption="**ʟɪsᴛ ʙᴏᴛ ʏᴀɴɢ sᴜᴅᴀʜ ᴅɪʙᴜᴀᴛ ᴀᴋᴛɪғ ᴀᴘᴀ ᴛɪᴅᴀᴋ...**")
    response = "**ʟɪsᴛ ʙᴏᴛ ʏᴀɴɢ sᴜᴅᴀʜ ᴅɪʙᴜᴀᴛ ᴀᴋᴛɪғ ᴀᴘᴀ ᴛɪᴅᴀᴋ**\n\n"
    for bot_username in BOT_LIST:
        try:
            bot = await app.get_users(bot_username)
            bot_id = bot.id
            await asyncio.sleep(0.5)
            bot_info = await app.send_message(bot_id, "/start")
            await asyncio.sleep(3)
            async for bot_message in app.get_chat_history(bot_id, limit=1):
                if bot_message.from_user.id == bot_id:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✅**\n\n"
                else:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**\n\n"
        except Exception:
            response += f"╭⎋ {bot_username}\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✅**\n"
    
    await msg.edit_text(response)
                
