from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from config import token
from config import proxy_token

def do_start(bot: Bot, update: Updater):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "Напиши тут что-нибудь!",
    )


def do_echo(bot, update):
    text = update.message.text
    bot.send_message(
        chat_id = update.message.chat_id,
        text = text,
    )



def main():
    bot = Bot(
        token = token,
        base_url = proxy_token,
    )
    updater = Updater(
        bot = bot
    )


    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)


    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)


    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
