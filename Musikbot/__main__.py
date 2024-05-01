import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Musikbot import LOGGER, app, userbot
from Musikbot.core.call import DAXX
from Musikbot.misc import sudo
from Musikbot.plugins import ALL_MODULES
from Musikbot.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("String sessions failed, silahkan ulang")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Musikbot.plugins" + all_module)
    LOGGER("Musikbot.plugins").info("Moduls Done...")
    await userbot.start()
    await DAXX.start()
    try:
        await DAXX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Musikbot").error(
            "Start vidio call group\channels\n\nStop........"
        )
        exit()
    except:
        pass
    await DAXX.decorators()
    LOGGER("Musikbot").info(
        "By Joox"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Musikbot").info("Stop Music..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
