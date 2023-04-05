import os

from flask import Flask, redirect
from flask_discord import DiscordOAuth2Session

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Development only
discord = DiscordOAuth2Session(app)


@app.route('/login')
def login():
    return discord.create_session()


@app.route('/callback')
def callback():
    discord.callback()
    return redirect('/')
