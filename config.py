import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 1458059))
API_HASH = getenv("API_HASH", "f1c4e91f5e9f4d8637c8233091499068")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6829929730:AAEadyQRsl-QdrDZoflkapQIXVAyXqQjb9w")
BOT_USERNAME = getenv("BOT_USERNAME")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://venomrapidcool:Priyaislove@cluster0.j7abkse.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 1195997736))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/CoderXKrishna/Arank_Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Mrs_And_Mr_Hitler")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Mrs_And_Mr_Hitler")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQAWP4sAiMxovers1BRp6LdyN1mwYPdg0UcWHx9q-pJMGFJBP4i9rG2FrnPOZW9QXFBd9NrZF1hraQNlgphZVSRfLW42rhgcz7IiWtOTgtA9ue1qP_88BROyM-8vYW9rae66U0EtvbwJ-dPhPJ0KxbqadWHxLwPBTtu38Gdjf8k9-KycjprehIk4AeJG5Q8S4-PmlvgZejAfpqtRnDTKICZEjtcEoTOvzNgHIyFoig0-8nkyZGqIib3K_u0njYJeakvblhkrvxmz4uadmYOn2hw0A0S1CIV92IuJ0V1F9CbpIe2nDC2OSmCbQlSEXmMXpl6Uj4VDjna0zEWWQk_Bn6OP1lPExQAAAAFLfLXrAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/7e7889dd8842e04cbab3b.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/36caf45b45a45ea368434.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/36caf45b45a45ea368434.jpg"
STATS_IMG_URL = "https://telegra.ph/file/36caf45b45a45ea368434.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/36caf45b45a45ea368434.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/58f52417365f7f8622e02.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/58f52417365f7f8622e02.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/7e7889dd8842e04cbab3b.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/7e7889dd8842e04cbab3b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/58f52417365f7f8622e02.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/58f52417365f7f8622e02.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/58f52417365f7f8622e02.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
