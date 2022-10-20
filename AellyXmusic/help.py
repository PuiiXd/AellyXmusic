# Aelly [@AellyOfficial
# Don't remove credits ⚠️

import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 Hoi {m.from_user.mention}!

🛠 MUSIC PLAYER HELP MENU

⚡ COMMANDS FOR EVERYONE
• {HNDLR}play [song title | youtube link | reply audio file] - to play the song
• {HNDLR}videoplay [video title | youtube link | reply video file] - to play video
• {HNDLR}playlist to view playlist
• {HNDLR}ping - to check status
• {HNDLR}id - to see user id
• {HNDLR}video - video title | youtube link to search video
• {HNDLR}song - song title | youtube link to search for songs
• {HNDLR}help - to see a list of commands
• {HNDLR}join- to join | to group 

⚡ COMMANDS FOR ALL ADMINS
• {HNDLR}resume - to continue playing a song or video
• {HNDLR}pause - to pause the playback of a song or video
• {HNDLR}skip - to skip songs or videos
• {HNDLR}end - to end playback</b>
"""
    await m.reply(HELP)
