""" t.me/hse_python_2021_bot """

import base64
import logging
import random

from telegram import Update, User
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

BOT_TOKEN = ''

EXAM_RESULT = [
    'Ты сдашь экзамен!',
    'Потрачено! Шансов нет, но вы держитесь',
    'Все операторы на линии заняты! Вам ответит первый освободившийся оператор.'
]

MESSAGES_STAT = {}


def up_messages_stat(user: User) -> None:
    current_user = MESSAGES_STAT.get(user.id)
    if current_user:
        current_user['count'] += 1
    else:
        MESSAGES_STAT[user.id] = {'login': user.username, 'count': 1}


def start(update: Update, _: CallbackContext) -> None:
    """ Send a message when the command /start is issued. """
    user = update.message.from_user

    update.message.reply_text(f'Hello, {user.username}. {user.first_name} {user.last_name}')


def help_command(update: Update, _: CallbackContext) -> None:
    """ Send a message when the command /help is issued. """
    update.message.reply_text('Help!')


def echo(update: Update, _: CallbackContext) -> None:
    """ Echo the user message. """
    message = update.message.text
    up_messages_stat(update.message.from_user)

    if 'экзамен' in message.lower():
        reply_message = random.choice(EXAM_RESULT)
    else:
        reply_message = message
    update.message.reply_text(reply_message)


def get_bot_stat(update: Update, _: CallbackContext) -> None:
    reply_message = 'User stats:\n\n'
    for user in MESSAGES_STAT.values():
        reply_message += f"{user['login']} - {user['count']}\n"

    update.message.reply_text(reply_message)


def main() -> None:
    """Start the bot."""
    updater = Updater(base64.b64decode(BOT_TOKEN).decode())
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(CommandHandler('stat', get_bot_stat))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
