from telegram.ext import Updater, CommandHandler
import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler  # Add this line

# Load environment variables from .env file
load_dotenv()

# ... (rest of your code)

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
