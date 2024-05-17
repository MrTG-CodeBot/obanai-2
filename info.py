import re
import os
from os import environ
from pyrogram import enums

import asyncio
import json
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default

# basic information
API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')

# for the main bot
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

# for the photo saver bot
BOT_TOKEN_2 = os.environ.get('BOT_TOKEN', '')

PORT = os.environ.get("PORT", "8080")
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
REQUESTED_CHANNEL = int(os.environ.get("REQUESTED_CHANNEL", ""))
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)

# for force subscribe[Your Force Sub Channel Username Without @ (eg:- sd_bots)]
F_SUB = os.environ.get("FORCE_SUB", "") 

# for eval function, work only in a specific group
EVAL_ID = int(os.environ.get("EVAL_ID", ""))

# for message forward from user
ADMIN_GROUP_ID = int(environ.get('ADMIN_GROUP_ID', ''))

# important information for your bot
S_GROUP = environ.get('S_GROUP', "")
S_CHANNEL = environ.get('S_CHANNEL', "")

# for the pic saver bot 
PIC_LOG_CHANNEL = int(os.environ.get("PIC_LOG_CHANNEL", ""))

# for mongodb and for the main bot
DATABASE_NAME = os.environ.get("DATABASE_NAME", "")     
DATABASE_URI  = os.environ.get("DATABASE_URI", "")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = os.environ.get('MONGO_URL', "")

# for the photo saver bot
DATABASE_NAME_2 = os.environ.get("DATABASE_NAME_2", "")
DATABASE_URI_2 = os.environ.get("DATABASE_URI_2", "")

# for google ai 
# how to get the api key == https://t.me/sd_bots/256 (copy this link and search on telegram)
GOOGLE_API_KEY = os.environ.get('API_KEY', '')

#for spotify 
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID', '')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET', '')
