from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import *
from DAXXMUSIC import app
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.utils import bot_sys_stats
from DAXXMUSIC.utils.decorators.language import language
from DAXXMUSIC.utils.inline import supp_markup
from config import BANNED_USERS


@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await DAXX.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
