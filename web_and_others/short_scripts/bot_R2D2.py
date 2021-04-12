import config
import telebot
bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types='text')
