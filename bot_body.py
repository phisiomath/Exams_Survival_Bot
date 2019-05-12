import telegram.ext
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async
import config
import handlers

updater = Updater(token=config.bot_token, workers=100)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)



def main():
    dispatcher.add_handler(handlers.start_handler)
    dispatcher.add_handler(handlers.help_handler)
    dispatcher.add_handler(handlers.callback_handler)
    dispatcher.add_handler(handlers.plain_handler)
    updater.start_polling()
    return 0


if __name__ == '__main__':
    main()
