from Musikbot import app
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from logging import getLogger
from Musikbot.utils.daxx_ban import admin_filter
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from Musikbot.utils.database import add_served_chat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Musikbot.utils.database import get_assistant
import asyncio
from Musikbot.misc import SUDOERS
from Musikbot.mongo.afkdb import PROCESS
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from Musikbot import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from Musikbot.utils.database import get_assistant, is_active_chat



random_photo = [
    "https://mallucampaign.in/images/img_1709026510.jpg",
    "https://mallucampaign.in/images/img_1709026510.jpg",
    "https://mallucampaign.in/images/img_1709026510.jpg",
]
# --------------------------------------------------------------------------------- #





LOGGER = getLogger(__name__)

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        if chat_id not in self.data:
            self.data[chat_id] = {"state": "on"}  # Default state is "on"

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None



def circle(pfp, size=(500, 500), brightness_factor=10):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    pfp = ImageEnhance.Brightness(pfp).enhance(brightness_factor)
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname, brightness_factor=1.3):
    background = Image.open("Musikbot/assets/wel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp, brightness_factor=brightness_factor) 
    pfp = pfp.resize((512, 512))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('Musikbot/assets/font.ttf', size=70)
    welcome_font = ImageFont.truetype('Musikbot/assets/font.ttf', size=61)
    #draw.text((630, 540), f'ID: {id}', fill=(255, 255, 255), font=font)
    #
 #   draw.text((630, 300), f'NAME: {user}', fill=(255, 255, 255), font=font)
    draw.text((630, 450), f'ID: {id}', fill=(255, 255, 255), font=font)
#    draw.text((630, 150), f"{chatname}", fill=(225, 225, 225), font=welcome_font)
  #  draw.text((630, 230), f"USERNAME : {uname}", fill=(255, 255, 255), font=font)

    #
    pfp_position = (48, 88)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"


@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    usage = "**Usage:**\n**/welcome [on|off]**"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "off":
            if A:
                await message.reply_text("**Pesan selamat datang berhasil di matikan!**")
            else:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(f"**Pesan selamat datang tidak akan muncul di** {message.chat.title}")
        elif state == "on":
            if not A:
                await message.reply_text("**Pesan selamat datang berhasil di hidupkan**")
            else:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(f"**Berhasil menghidupkan pesan selamat datang dengan notifikasi** {message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("**Hanya admin yang berhak menghidupkan pesan selamat datang!**")



@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    count = await app.get_chat_members_count(chat_id)
    A = await wlcm.find_one(chat_id)
    if A:
        return

    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    
    # Add the modified condition here
    if member.new_chat_member and not member.old_chat_member and member.new_chat_member.status != "kicked":
    
        try:
            pic = await app.download_media(
                user.photo.big_file_id, file_name=f"pp{user.id}.png"
            )
        except AttributeError:
            pic = "Musikbot/assets/upic.png"
        if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
            try:
                await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
            except Exception as e:
                LOGGER.error(e)
        try:
            welcomeimg = welcomepic(
                pic, user.first_name, member.chat.title, user.id, user.username
            )
            button_text = "Lihat Members"
            add_button_text = "ɪɴғᴏ"
            deep_link = f"tg://openmessage?user_id={user.id}"
            add_link = f"https://t.me/{app.username}?startgroup=true"
            temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
                member.chat.id,
                photo=welcomeimg,
                caption=f"""
**Hi Selamat Datang**

**Nama :** {user.mention}
**Id :** `{user.id}`
**Username :** @{user.username}
**Total members :** {count}

""",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(button_text, url=deep_link)],
                    [InlineKeyboardButton(text=add_button_text, url=add_link)],
                ])
            )
        except Exception as e:
            LOGGER.error(e)


@app.on_message(filters.command("gadd") & filters.user(963826795))
async def add_all(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply("**format perintah tidak valid, silakan gunakan `/gadd bot username`**")
        return
    
    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply(" **Menambahkan bot yang diberikan ke semua obrolan**")
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1002107353194:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**Menambahkan {bot_username}**\n\n**Menambahkan {done} Chats**\n**➥ Gagal masuk {failed} Chats ❌**\n\n**Ditambahkan Oleh** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**Menambahkan {bot_username}**\n\n**Menambahkan {done} Chat ✅**\n**Gagal Menambahkan {failed} Chat ❌**\n\n**Ditambahkan oleh** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits
        
        await lol.edit(
            f"**{bot_username} Bot berhasil ditambahkan **\n\n**Menambahkan {done} Chat ✅**\n**Gagal Menambahkan {failed} Chats❌**\n\n**Ditambahkan Oleh** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
