import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

# Load environment variables from .env file
load_dotenv()

# Replace "YOUR_BOT_TOKEN" with your actual Telegram bot token
bot_token = os.environ.get("6563388880:AAEePBpgrmEOsEC2D3VB8QnF3ADiEIK87Hk")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot.")

def main() -> None:
    updater = Updater("6563388880:AAEePBpgrmEOsEC2D3VB8QnF3ADiEIK87Hk")
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("verify", verify, pass_args=True))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
