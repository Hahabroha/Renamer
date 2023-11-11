import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

# Load environment variables from .env file
load_dotenv()

# Replace "YOUR_ACTUAL_BOT_TOKEN" with your real bot token
bot_token = os.environ.get("6563388880:AAEePBpgrmEOsEC2D3VB8QnF3ADiEIK87Hk")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot.")

def verify(update, context):
    user = update.effective_user
    original_link = context.args[0] if context.args else None

    # Your verification logic here

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Verification logic executed. Original link: {original_link}",
    )

def main() -> None:
    updater = Updater(token=bot_token)
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("verify", verify, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
