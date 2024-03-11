import random 
from pyrogram import filters,Client,enums
from Musikbot import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions
from Musikbot.mongo.nightmodedb import nightdb,nightmode_on,nightmode_off,get_nightchats 



CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages = False,
    can_send_other_messages = False,
    can_send_polls = False,
    can_change_info = False,
    can_add_web_page_previews = False,
    can_pin_messages = False,
    can_invite_users = False )


OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages = True,
    can_send_other_messages = True,
    can_send_polls = True,
    can_change_info = True,
    can_add_web_page_previews = True,
    can_pin_messages = True,
    can_invite_users = True )
    
buttons = InlineKeyboardMarkup([[InlineKeyboardButton("Enable", callback_data="add_night"),InlineKeyboardButton("Disable", callback_data="rm_night")]])         

@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(photo="https://mallucampaign.in/images/img_1710090470.jpg", caption="**Silahkan klik tombol diatas mode malam mau di aktifkan apa tidak..**",reply_markup=buttons)
              
     
@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query : CallbackQuery):
    data = query.data 
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id" : chat_id})
    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
    if user_id in administrators:   
        if data == "add_night":
            if check_night:        
                await query.message.edit_caption("**Mode malam berhasil di aktifkan di group chat.**")
            elif not check_night :
                await nightmode_on(chat_id)
                await query.message.edit_caption("**Tambahkan obrolan ke database saya. grup ini akan ditutup pada pukul 12 pagi [IST] dan akan dibuka pada pukul 06 pagi [IST] .**") 
        if data == "rm_night":
            if check_night:  
                await nightmode_off(chat_id)      
                await query.message.edit_caption("**Mode malam  dihapus dari database saya!**")
            elif not check_night:
                await query.message.edit_caption("**Mode malam sudah dinonaktifkan dalam obrolan ini**") 
            
    
    
async def start_nightmode() :
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for add_chat in chats:
        try:
            await app.send_photo(
                add_chat,
                photo="https://mallucampaign.in/images/img_1710090470.jpg",
                caption= f"**ᴍᴀʏ ᴛʜᴇ ᴀɴɢᴇʟs ғʀᴏᴍ ʜᴇᴀᴠᴇɴ ʙʀɪɴɢ ᴛʜᴇ sᴡᴇᴇᴛᴇsᴛ ᴏғ ᴀʟʟ ᴅʀᴇᴀᴍs ғᴏʀ ʏᴏᴜ. ᴍᴀʏ ʏᴏᴜ ʜᴀᴠᴇ ʟᴏɴɢ ᴀɴᴅ ʙʟɪssғᴜʟ sʟᴇᴇᴘ ғᴜʟʟ ᴏғ ʜᴀᴘᴘʏ ᴅʀᴇᴀᴍs.\n\nɢʀᴏᴜᴘ ɪs ᴄʟᴏsɪɴɢ ɢᴏᴏᴅ ɴɪɢʜᴛ ᴇᴠᴇʀʏᴏɴᴇ  !**")
            
            await app.set_chat_permissions(add_chat,CLOSE_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To close Group {add_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.start()

async def close_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for rm_chat in chats:
        try:
            await app.send_photo(
                rm_chat,
                photo="https://mallucampaign.in/images/img_1710090470.jpg",
                caption= f"**ɢʀᴏᴜᴘ ɪs ᴏᴘᴇɴɪɴɢ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴇᴠᴇʀʏᴏɴᴇ !\n\nᴍᴀʏ ᴛʜɪs ᴅᴀʏ ᴄᴏᴍᴇ ᴡɪᴛʜ ᴀʟʟ ᴛʜᴇ ʟᴏᴠᴇ ʏᴏᴜʀ ʜᴇᴀʀᴛ ᴄᴀɴ ʜᴏʟᴅ ᴀɴᴅ ʙʀɪɴɢ ʏᴏᴜ ᴇᴠᴇʀʏ sᴜᴄᴄᴇss ʏᴏᴜ ᴅᴇsɪʀᴇ. Mᴀʏ ᴇᴀᴄʜ ᴏғ ʏᴏᴜʀ ғᴏᴏᴛsᴛᴇᴘs ʙʀɪɴɢ Jᴏʏ ᴛᴏ ᴛʜᴇ ᴇᴀʀᴛʜ ᴀɴᴅ ʏᴏᴜʀsᴇʟғ. ɪ ᴡɪsʜ ʏᴏᴜ ᴀ ᴍᴀɢɪᴄᴀʟ ᴅᴀʏ ᴀɴᴅ ᴀ ᴡᴏɴᴅᴇʀғᴜʟ ʟɪғᴇ ᴀʜᴇᴀᴅ.**")
            
            await app.set_chat_permissions(rm_chat,OPEN_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To open Group {rm_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1)
scheduler.start()



