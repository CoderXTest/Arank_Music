from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🥺",
                url=f"https://t.me/Arank_Music_Bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🥺",
                url=f"https://t.me/Arank_Music_Bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="♢ ʜᴇʟᴩ ♢", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="♡ sᴜᴩᴩᴏʀᴛ ♡", url="https://t.me/Mr_Mrs_Krishna"
            ),
            InlineKeyboardButton(
                text="✗ ᴍᴀɪɴᴛᴀɪɴᴇʀ ✗", user_id=1195997736
            )
        ],
     ]
    return buttons
