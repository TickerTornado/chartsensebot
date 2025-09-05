from telegram.ext import Application, CommandHandler
import os
from dotenv import load_dotenv
from commands import start, help, chartink, screener, setalert, listalerts

# Load environment variables
load_dotenv()

def main():
    """Start the bot."""
    application = Application.builder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()
    application.add_handler(CommandHandler("start", start.start_command))
    application.add_handler(CommandHandler("help", help.help_command))
    application.add_handler(CommandHandler("chartink", chartink.chartink_command))
    application.add_handler(CommandHandler("screener", screener.screener_command))
    application.add_handler(CommandHandler("setalert", setalert.setalert_command))
    application.add_handler(CommandHandler("listalerts", listalerts.listalerts_command))
    application.run_polling()

if __name__ == '__main__':
    main()
