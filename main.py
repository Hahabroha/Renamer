from bot import Bot
def main() -> None:
    updater = Updater("6563388880:AAEePBpgrmEOsEC2D3VB8QnF3ADiEIK87Hk")
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("verify", verify, pass_args=True))  # Add this line

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
