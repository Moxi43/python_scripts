import os, time, random

import telebot

import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            #Отправляем вслед за файлом его file.id
            bot.send_message(message.chat.id, message.voice.file_id, reply_to_message_id = msg.message_id)
        time.sleep(3)

if __name__ == '__main__':
    bot.polling(none_stop = True)
