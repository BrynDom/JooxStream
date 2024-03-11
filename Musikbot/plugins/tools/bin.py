from ... import *
from pyrogram import *
from pyrogram.types import *


@app.on_message(filters.command(["bin", "ccbin", "bininfo"], [".", "!", "/"]))
async def check_ccbin(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b>Please Give Me a Bin To\nGet Bin Details !</b>"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("<b>Checking ...</b>")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("<b>❌ Wrong Bin❗...</b>")
    try:
        resp = await api.bininfo(bin)
        await aux.edit(f"""
<b> TEMPAT YANG VALID  ✅</b>

<b>🏦 BANK</b> <tt>{resp.bank}</tt>
<b>💳 BIN</b> <tt>{resp.bin}</tt>
<b>🏡 NEGARA </b> <tt>{resp.country}</tt>
<b>BENDERA </b> <tt>{resp.flag}</tt>
<b>ISO</b> <tt>{resp.iso}</tt>
<b>LEVEL/b> <tt>{resp.level}</tt>
<b>PREPAID </b> <tt>{resp.prepaid}</tt>
<b>TYPE </b> <tt>{resp.type}</tt>
<b>VENDOR </b> <tt>{resp.vendor}</tt>"""
        )
    except:
        return await aux.edit(f"""
🚫 BIN tidak dikenali. Silakan masukkan BIN yang valid.""")
