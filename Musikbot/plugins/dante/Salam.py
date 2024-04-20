
from time import sleep
from . import (
    eor,
    app,
)

@app.on_message(pattern="ass$")
async def _(event):
    await event.eor("**Assalamu'alaikum Warohmatulohi Wabarokatu**")


@app.on_message(pattern="as$")
async def _(event):
    await event.eor("**Assalamu'alaikum**")
    
@app.on_message(pattern="ws$")
async def _(event):
    await event.eor("**Wa'alaikumussalam**")

    
@app.on_message(pattern="ks$")
async def _(event):
    xx = await event.eor("**Hy kaa 🥹**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@app.on_message(pattern="jws$")
async def _(event):
    xx = await event.eor(event, "**Astaghfirullah, Jawab dulu salam dong**")
    sleep(2)
    await xx.edit("**Assalamu'alaikum**")


@app.on_message(pattern="3x$")
async def _(event):
    xx = await event.eor("**Bismillah, 3x**")
    sleep(2)
    await xx.edit("**Assalamu'alaikum Bisa yug Kali**")
    
@app.on_message(pattern="kg$")
async def _(event):
    xx = await event.eor("**Nih Gw Pantun,Buah Apel Buah Kedondong**")
    sleep(2)
    await xx.edit("**Senggol Dong!!!**")

@app.on_message(pattern="hm$")
async def _(event):
    xx = await event.eor("**Batuk dulu g sih**")
    sleep(2)
    await xx.edit("**Biar ludah batuk nya gw ludahin ke wajah lu!**")
