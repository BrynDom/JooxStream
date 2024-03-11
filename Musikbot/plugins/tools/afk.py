import time, re
from config import BOT_USERNAME
from pyrogram.enums import MessageEntityType
from pyrogram import filters
from pyrogram.types import Message
from Musikbot import app
from Musikbot.mongo.readable_time import get_readable_time
from Musikbot.mongo.AFKdb import add_AFK, is_AFK, remove_AFK



@app.on_message(filters.command(["AFK", "brb"], prefixes=["/", "!"]))
async def active_AFK(_, message: Message):
    if message.sender_chat:
        return
    user_id = message.from_user.id
    verifier, reasondb = await is_AFK(user_id)
    if verifier:
        await remove_AFK(user_id)
        try:
            AFKtype = reasondb["type"]
            timeAFK = reasondb["time"]
            data = reasondb["data"]
            reasonAFK = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeAFK)))
            if AFKtype == "text":
                send = await message.reply_text(
                    f"**{message.from_user.first_name}**Kembali online dan tidak aktif selama {seenago}",
                    disable_web_page_preview=True,
                )
            if AFKtype == "text_reason":
                send = await message.reply_text(
                    f"**{message.from_user.first_name}**Kembali online dan tidak aktif selama {seenago}\n\n alasan : `{reasonAFK}`",
                    disable_web_page_preview=True,
                )
            if AFKtype == "animation":
                if str(reasonAFK) == "None":
                    send = await message.reply_animation(
                        data,
                        caption=f"**{message.from_user.first_name}**kembali online dan tidak aktif selama  {seenago}",
                    )
                else:
                    send = await message.reply_animation(
                        data,
                        caption=f"**{message.from_user.first_name}**kembali online dan pergi  {seenago}\n\nalasan: `{reasonAFK}`",
                    )
            if AFKtype == "photo":
                if str(reasonAFK) == "None":
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"**{message.from_user.first_name}**Kembali online dan tidak aktif selama {seenago}",
                    )
                else:
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"**{message.from_user.first_name}**Kembali online dan pergi {seenago}\n\nalasan: `{reasonAFK}`",
                    )
        except Exception:
            send = await message.reply_text(
                f"**{message.from_user.first_name}**Kembali online",
                disable_web_page_preview=True,
            )

    if len(message.command) == 1 and not message.reply_to_message:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and not message.reply_to_message:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "text_reason",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        _reason = message.text.split(None, 1)[1].strip()
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.sticker:
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
    elif len(message.command) > 1 and message.reply_to_message.sticker:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text_reason",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
    else:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }

    await add_AFK(user_id, details)    
    await message.reply_text(f"{message.from_user.first_name} Sekarang AFK!")




chat_watcher_group = 1


@app.on_message(
    ~filters.me & ~filters.bot & ~filters.via_bot,
    group=chat_watcher_group,
)
async def chat_watcher_func(_, message):
    if message.sender_chat:
        return
    userid = message.from_user.id
    user_name = message.from_user.first_name
    if message.entities:
        possible = ["/AFK", f"/AFK@{BOT_USERNAME}"]
        message_text = message.text or message.caption
        for entity in message.entities:
            if entity.type == MessageEntityType.BOT_COMMAND:
                if (message_text[0 : 0 + entity.length]).lower() in possible:
                    return

    msg = ""
    replied_user_id = 0


    
    verifier, reasondb = await is_AFK(userid)
    if verifier:
        await remove_AFK(userid)
        try:
            AFKtype = reasondb["type"]
            timeAFK = reasondb["time"]
            data = reasondb["data"]
            reasonAFK = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeAFK)))
            if AFKtype == "text":
                msg += f"**{user_name[:25]}** kembali online dan tidak aktif selama  {seenago}\n\n"
            if AFKtype == "text_reason":
                msg += f"**{user_name[:25]}**kembali online dan tidak aktif selama {seenago}\n\nalasan: `{reasonAFK}`\n\n"
            if AFKtype == "animation":
                if str(reasonAFK) == "None":
                    send = await message.reply_animation(
                        data,
                        caption=f"**{user_name[:25]}** Kembali online dan tidak aktif selama  {seenago}\n\n",
                    )
                else:
                    send = await message.reply_animation(
                        data,
                        caption=f"**{user_name[:25]}** kembali online dan tidak aktif selama {seenago}\n\nalasan: `{reasonAFK}`\n\n",
                    )
            if AFKtype == "photo":
                if str(reasonAFK) == "None":
                    send = await message.reply_photo(
                        photo=f"downloads/{userid}.jpg",
                        caption=f"**{user_name[:25]}** kembali online dan tidak aktif {seenago}\n\n",
                    )
                else:
                    send = await message.reply_photo(
                        photo=f"downloads/{userid}.jpg",
                        caption=f"**{user_name[:25]}** kembali online dan tidak aktif selama {seenago}\n\nalasan: `{reasonAFK}`\n\n",
                    )
        except:
            msg += f"**{user_name[:25]}** Kembali online\n\nSelamat datang kembali!"


    if message.reply_to_message:
        try:
            replied_first_name = message.reply_to_message.from_user.first_name
            replied_user_id = message.reply_to_message.from_user.id
            verifier, reasondb = await is_AFK(replied_user_id)
            if verifier:
                try:
                    AFKtype = reasondb["type"]
                    timeAFK = reasondb["time"]
                    data = reasondb["data"]
                    reasonAFK = reasondb["reason"]
                    seenago = get_readable_time((int(time.time() - timeAFK)))
                    if AFKtype == "text":
                        msg += (
                            f"**{replied_first_name[:25]}**Sedang AFK online {seenago}\n\n"
                        )
                    if AFKtype == "text_reason":
                        msg += f"**{replied_first_name[:25]}**Telah AFK sejak itu {seenago}\n\nalasan: `{reasonAFK}`\n\n"
                    if AFKtype == "animation":
                        if str(reasonAFK) == "None":
                            send = await message.reply_animation(
                                data,
                                caption=f"**{replied_first_name[:25]}**ᴇ {seenago}\n\n",
                            )
                        else:
                            send = await message.reply_animation(
                                data,
                                caption=f"**{replied_first_name[:25]}**Telah AFK sejak {seenago}\n\nalasan: `{reasonAFK}`\n\n",
                            )
                    if AFKtype == "photo":
                        if str(reasonAFK) == "None":
                            send = await message.reply_photo(
                                photo=f"downloads/{replied_user_id}.jpg",
                                caption=f"**{replied_first_name[:25]}**Telah kembali sejak {seenago}\n\n",
                            )
                        else:
                            send = await message.reply_photo(
                                photo=f"downloads/{replied_user_id}.jpg",
                                caption=f"**{replied_first_name[:25]}**Telah AFK sejak itu  {seenago}\n\nalasan: `{reasonAFK}`\n\n",
                            )
                except Exception:
                    msg += f"**{replied_first_name}**Telah AFK\ntunggu.\n\n"
        except:
            pass

    if message.entities:
        entity = message.entities
        j = 0
        for x in range(len(entity)):
            if (entity[j].type) == MessageEntityType.MENTION:
                found = re.findall("@([_0-9a-zA-Z]+)", message.text)
                try:
                    get_user = found[j]
                    user = await app.get_users(get_user)
                    if user.id == replied_user_id:
                        j += 1
                        continue
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_AFK(user.id)
                if verifier:
                    try:
                        AFKtype = reasondb["type"]
                        timeAFK = reasondb["time"]
                        data = reasondb["data"]
                        reasonAFK = reasondb["reason"]
                        seenago = get_readable_time((int(time.time() - timeAFK)))
                        if AFKtype == "text":
                            msg += (
                                f"**{user.first_name[:25]}** sudah AFK sejak itu {seenago}\n\n"
                            )
                        if AFKtype == "text_reason":
                            msg += f"**{user.first_name[:25]}** Telah AFK sejak itu  {seenago}\n\nalasan: `{reasonAFK}`\n\n"
                        if AFKtype == "animation":
                            if str(reasonAFK) == "None":
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**{user.first_name[:25]}** Telah AFK sejak {seenago}\n\n",
                                )
                            else:
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**{user.first_name[:25]}** Telah AFK sejak {seenago}\n\nalasan: `{reasonAFK}`\n\n",
                                )
                        if AFKtype == "photo":
                            if str(reasonAFK) == "None":
                                send = await message.reply_photo(
                                    photo=f"downloads/{user.id}.jpg",
                                    caption=f"**{user.first_name[:25]}** Telah AFK sejak {seenago}\n\n",
                                )
                            else:
                                send = await message.reply_photo(
                                    photo=f"downloads/{user.id}.jpg",
                                    caption=f"**{user.first_name[:25]}** Telah AFK sejak {seenago}\n\nalasan: `{reasonAFK}`\n\n",
                                )
                    except:
                        msg += f"**{user.first_name[:25]}** ɪs ᴀғᴋ\n\n"
            elif (entity[j].type) == MessageEntityType.TEXT_MENTION:
                try:
                    user_id = entity[j].user.id
                    if user_id == replied_user_id:
                        j += 1
                        continue
                    first_name = entity[j].user.first_name
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_AFK(user_id)
                if verifier:
                    try:
                        AFKtype = reasondb["type"]
                        timeAFK = reasondb["time"]
                        data = reasondb["data"]
                        reasonAFK = reasondb["reason"]
                        seenago = get_readable_time((int(time.time() - timeAFK)))
                        if AFKtype == "text":
                            msg += f"**{first_name[:25]}** Telah AFK sejak {seenago}\n\n"
                        if AFKtype == "text_reason":
                            msg += f"**{first_name[:25]}** Telah AFK sejak {seenago}\n\nalasan: `{reasonAFK}`\n\n"
                        if AFKtype == "animation":
                            if str(reasonAFK) == "None":
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**{first_name[:25]}** Telah AFK sejak {seenago}\n\n",
                                )
                            else:
                                send = await message.reply_animation(
                                    data,
                                    caption=f"**{first_name[:25]}** Telah AFK sejak {seenago}\n\nalasan: `{reasonAFK}`\n\n",
                                )
                        if AFKtype == "photo":
                            if str(reasonAFK) == "None":
                                send = await message.reply_photo(
                                    photo=f"downloads/{user_id}.jpg",
                                    caption=f"**{first_name[:25]}** Telah AFK sejak  {seenago}\n\n",
                                )
                            else:
                                send = await message.reply_photo(
                                    photo=f"downloads/{user_id}.jpg",
                                    caption=f"**{first_name[:25]}** Telah AFK sejak  {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonAFK}`\n\n",
                                )
                    except:
                        msg += f"**{first_name[:25]}** ɪs ᴀғᴋ\n\n"
            j += 1
    if msg != "":
        try:
            send = await message.reply_text(msg, disable_web_page_preview=True)
        except:
            return







