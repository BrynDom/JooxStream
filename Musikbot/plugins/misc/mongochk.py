from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from DAXXMUSIC import app as DAXX


mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')


@DAXX.on_message(filters.command("mongochk"))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("Silakan masukkan URL MongoDB Anda setelah perintah. Example: /mongochk your_mongodb_url")
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("MongoDB URL benar, Berhasil disambungkan ✅")
        except Exception as e:
            await message.reply(f"Gagal tersambung ke MongoDB: {e}")
    else:
        await message.reply("URL MongoDB salah!")
