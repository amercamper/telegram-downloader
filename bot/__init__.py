import logging
from os import getenv, mkdir

from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

if getenv('DEBUG') == "1":
    logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=logging.ERROR)

ADMINS = getenv('@jawfe').split()
BASE_FOLDER = getenv('/data')
DL_FOLDER = BASE_FOLDER

try:
    mkdir(DL_FOLDER)
except FileExistsError:
    pass
except:
    logging.error('Failed to create data storage path!')
    exit(1)

app = Client(
    name='TDownloader',
    api_id=int(getenv('21211387')),
    api_hash=getenv('82767b47d8c3d45a00fcf29cdbc7729f'),
    bot_token=getenv('7371147227:AAH6X5SQgkXrlpLxO48-trcjp81pOEJk0Tk')
)
