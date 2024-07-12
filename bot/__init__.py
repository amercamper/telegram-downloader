import logging
from os import getenv, mkdir

from dotenv import load_dotenv
from pyrogram import Client

# Load environment variables from .env file
load_dotenv()

# Configure logging based on DEBUG environment variable
if getenv('DEBUG') == "1":
    logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=logging.ERROR)

# Define ADMINS and BASE_FOLDER variables
ADMINS = getenv('ADMINS', '').split(',')
BASE_FOLDER = getenv('BASE_FOLDER', '/data')
DL_FOLDER = BASE_FOLDER

# Attempt to create data storage directory
try:
    mkdir(DL_FOLDER)
except FileExistsError:
    pass
except Exception as e:
    logging.error(f'Failed to create data storage path: {str(e)}')
    exit(1)

# Initialize Pyrogram Client
app = Client(
    'TDownloader',
    api_id=int(getenv('21211387')),
    api_hash=getenv('82767b47d8c3d45a00fcf29cdbc7729f'),
    bot_token=getenv('7371147227:AAH6X5SQgkXrlpLxO48-trcjp81pOEJk0Tk')
)
