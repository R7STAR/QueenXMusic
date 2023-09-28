from QueenX.core.bot import QueenXBot
from QueenX.core.dir import dirr
from QueenX.core.git import git
from QueenX.core.userbot import Userbot
from QueenX.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = QueenXBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
