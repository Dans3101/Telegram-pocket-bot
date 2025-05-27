from telegram.ext import ApplicationBuilder, CommandHandler
import os

async def start(update, context):
    await update.message.reply_text("Hello! Your Telegram Pocket Bot is running.")

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN is not set.")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
