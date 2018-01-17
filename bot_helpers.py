import os
import sys
from threading import Thread
from telegram.ext import Updater, CommandHandler, Filters

import handlers


def get_configured_updater():
    updater = Updater(os.environ.get('BOT_TOKEN'))

    updater.dispatcher.add_handler(
        CommandHandler('price', handlers.price_handler)
    )
    updater.dispatcher.add_error_handler(handlers.error)
    return updater


def add_restart_handler(updater, admin_username):
    def stop_and_restart():
        """
            Gracefully stop the Updater and replace the current
            process with a new one
        """
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(bot, update):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()

    updater.dispatcher.add_handler(
        CommandHandler(
            'r',
            restart,
            filters=Filters.user(username=admin_username)
        )
    )
    updater.dispatcher.add_error_handler(handlers.error)


def start_bot(updater):
    updater.start_polling()
    updater.idle()
