from telegram.ext import Updater, CommandHandler
import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler  # Add this line

# Load environment variables from .env file
load_dotenv()

# ... (rest of your code)

def main() -> None:
    updater = Updater("YOUR_BOT_TOKEN")
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("verify", verify, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
