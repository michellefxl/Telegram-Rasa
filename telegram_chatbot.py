import os
import json
import requests
import logging
from pathlib import Path
from datetime import date

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, User
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater

session_id = 0

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

ROOT_DIRPATH = os.path.realpath(os.path.dirname(__file__))
LOG_DIRPATH = os.path.join(ROOT_DIRPATH, "logs")
if not os.path.isdir(LOG_DIRPATH):
    os.makedirs(LOG_DIRPATH)

def start(update: Update, context: CallbackContext) -> None:
    """Handle `/start` command."""
    global session_id
    session_id += 1

    for handler in LOGGER.handlers[:]:
        LOGGER.removeHandler(handler)

    log_dirpath = os.path.join(LOG_DIRPATH, str(date.today()))
    print(log_dirpath)
    os.makedirs(log_dirpath, exist_ok=True)
    file_handler = logging.FileHandler(
        os.path.join(log_dirpath, f"session={str(session_id).zfill(3)}.txt"))
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s", )
    file_handler.setFormatter(formatter)
    LOGGER.addHandler(file_handler)
    LOGGER.log(logging.INFO, f"Session ID: {session_id}")


def reply_text(update: Update, context: CallbackContext) -> None:
    """Reply to user´s text messages."""

    query = update.message.text

    # forwards user input from Telegram to Rasa
    # can change port to access different model
    r = requests.post('http://localhost:5005/webhooks/rest/webhook',
                      json={
                          "sender": session_id,
                          "message": query
                      })
    # print(r.json())
    data = json.loads(r.text)[0]
    update.message.reply_text(data['text'], parse_mode="markdown")

    # update log with time information
    LOGGER.log(logging.INFO, f"User: {query}")
    LOGGER.log(logging.INFO, f"Bot: {data['text']}")

def main() -> None:
    """Run the Telegram chatbot."""

    # Create the Updater with your chatbot API token
    # https://core.telegram.org/bots#how-do-i-create-a-bot
    updater = Updater("{INSERT BOT TOKEN}")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # On command handlers
    # Start conversation with /start to create log folder 
    dispatcher.add_handler(CommandHandler("start", start))

    # On message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_text))

    # Start the chatbot
    updater.start_polling()


if __name__ == "__main__":
    main()