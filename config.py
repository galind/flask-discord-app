import os


class Config:
    SECRET_KEY = os.urandom(12)
    DISCORD_CLIENT_ID = os.getenv('CLIENT_ID')
    DISCORD_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    DISCORD_REDIRECT_URI = os.getenv('REDIRECT_URI')
    DISCORD_BOT_TOKEN = os.getenv('BOT_TOKEN')
