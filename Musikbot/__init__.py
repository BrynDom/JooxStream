from Musikbot.core.bot import Anony
from Musikbot.core.dir import dirr
from Musikbot.core.git import git
from Musikbot.core.userbot import Userbot
from Musikbot.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
