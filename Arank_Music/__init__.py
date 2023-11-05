from Arank_Music.core.Aɾαɳƙ Mυʂιƈ import Neox
from Arank_Music.core.dir import dirr
from Arank_Music.core.git import git
from Arank_Music.core.userbot import Userbot
from Arank_Music.misc import dbb, heroku

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
