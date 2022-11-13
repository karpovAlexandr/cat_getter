import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("BOT_TOKEN")
assert TOKEN, "No bot token in .env file!"

CAT_URL = "https://cataas.com/cat"
DOG_URL = "https://dog.ceo/api/breeds/image/random"
