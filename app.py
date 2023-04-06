import os

from flask import Flask, redirect, url_for, render_template
from flask_discord import (
    DiscordOAuth2Session, Unauthorized, requires_authorization
)

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Development only
discord = DiscordOAuth2Session(app)


@app.errorhandler(Unauthorized)
def redirect_unauthorized(e):
    return redirect(url_for('login'))


@app.route('/')
@requires_authorization
def home():
    guilds = discord.fetch_guilds()
    return render_template('index.html', guilds=guilds)


@app.route('/login')
def login():
    return discord.create_session()


@app.route('/callback')
def callback():
    discord.callback()
    return redirect(url_for('home'))
