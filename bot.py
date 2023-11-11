import uvloop
uvloop.install()
import datetime
import logging
import logging.config
import sys
import os
from dotenv import load_dotenv
import requests


from pyrogram import Client


from config import *
from database import db
from database.users import filter_users
from helpers import temp
from utils import broadcast_admins, create_server, set_commands

# Get logging configurations
logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "shortener",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins"),
        )

    async def start(self):

        temp.START_TIME = datetime.datetime.now()
        await super().start()

        if UPDATE_CHANNEL:
            try:
                self.invite_link = await self.create_chat_invite_link(UPDATE_CHANNEL)
            except Exception:
                logging.error(
                    f"Make sure to make the bot in your update channel - {UPDATE_CHANNEL}"
                )
                sys.exit(1)

        me = await self.get_me()
        self.owner = await self.get_users(int(OWNER_ID))
        self.username = f"@{me.username}"
        temp.BOT_USERNAME = me.username
        temp.FIRST_NAME = me.first_name
        if not await db.get_bot_stats():
            await db.create_stats()

        banned_users = await filter_users({"banned": True})
        async for user in banned_users:
            temp.BANNED_USERS.append(user["user_id"])

        await set_commands(self)

        await broadcast_admins(self, "** Bot started successfully **")
        logging.info("Bot started")

        if WEB_SERVER:
            await create_server()
            logging.info("Web server started")
            logging.info("Pinging server")

    async def stop(self):
        await broadcast_admins(self, "** Bot Stopped Bye **")
        await super().stop()
        logging.info("Bot Stopped Bye")


def verify(update, context):
    user = update.effective_user
    original_link = context.args[0] if context.args else None

    # Hardcoded values for testing
    shortener_site = "zxlink.in"
    api_key = "89e367badb1ee93eab04dd64450e18393d77d302"

    try:
        # Debugging information
        print(f"Shortener Site: {shortener_site}")
        print(f"API Key: {api_key}")
        print(f"Original Link: {original_link}")

        # Make a basic request to the shortener site
        response = requests.get(shortener_site)
        response.raise_for_status()

        # Debugging information
        print("Request successful")

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Verification successful! Shortener site is accessible.",
        )
    except requests.RequestException as e:
        # Debugging information
        print(f"Request failed. Error: {str(e)}")

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Verification failed. Error: {str(e)}",
        )

