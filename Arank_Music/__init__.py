from Arank_Music.core.Arank_Music import Arank
from Arank_Music.core.dir import dirr
from Arank_Music.core.git import git
from Arank_Music.core.userbot import Userbot
from Arank_Music.misc import dbb, heroku

from .logging import LOGGER

# Assuming these functions are meant to be called here, they need to be properly defined or removed if not needed
dirr()
git()
dbb()
heroku()

# Assuming Arank and Userbot classes are defined in their respective modules
app = Arank()
userbot = Userbot()

from .platforms import *  # Importing all from the "platforms" module

# Assuming these APIs are classes defined in the respective modules
Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
