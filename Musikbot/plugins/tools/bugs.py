from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import OWNER_ID as owner_id
from Musikbot import app



def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@app.on_message(filters.command("bug"))
async def bugs(_, msg: Message):
    if msg.chat.username:
        chat_username = f"@{msg.chat.username}/`{msg.chat.id}`"
    else:
        chat_username = f"Private Grup/`{msg.chat.id}`"

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = (
        "[" + msg.from_user.first_name + "](tg://user?id=" + str(msg.from_user.id) + ")"
    )
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    

    bug_report = f"""
**#ʙᴜɢ : ** **tg://user?id={owner_id}**

**ʀᴇᴩᴏʀᴛᴇᴅ ʙʏ : ** **{mention}**
**ᴜsᴇʀ ɪᴅ : ** **{user_id}**
**ᴄʜᴀᴛ : ** **{chat_username}**

**ʙᴜɢ : ** **{bugs}**

**ᴇᴠᴇɴᴛ sᴛᴀᴍᴩ : ** **{datetimes}**"""

    if msg.chat.type == "private":
        await msg.reply_text("<b>Perintah ini hanya bisa dilakukan digrup.</b>")
        return

    if user_id == owner_id:
        if bugs:
            await msg.reply_text(
                "<b>apakah kamu komedikan aku, kamu adalah pemiliknya.</b>",
            )
            return
        else:
            await msg.reply_text("Pemilik!")
    elif user_id != owner_id:
        if bugs:
            await msg.reply_text(
                f"<b>Berhasil mereport bug: {bugs}</b>\n\n"
                "<b>Successful bug reported see support group !</b>",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Tutup", callback_data="close_data")]]
                ),
            )
            await app.send_photo(
                -1001627039023,
                photo="https://mallucampaign.in/images/img_1710090491.jpg",
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Lihat bug", url=f"{msg.link}")],
                        [
                            InlineKeyboardButton(
                                "Tutup", callback_data="close_send_photo"
                            )
                        ],
                    ]
                ),
            )
        else:
            await msg.reply_text(
                f"<b>Tidak ada bug yang dilaporkan!</b>",
            )




@app.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(_,  query :CallbackQuery):
    is_admin = await app.get_chat_member(query.message.chat.id, query.from_user.id)
    if not is_admin.privileges.can_delete_messages:
        await query.answer("Anda tidak mempunyai hak untuk menutup ini.", show_alert=True)
    else:
        await query.message.delete()


