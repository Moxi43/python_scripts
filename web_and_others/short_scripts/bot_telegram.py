import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands = ['start', 'help'])
def handle_start_help(message):
    pass

@bot.message_handler(content_types = ['document', 'audio'])
def handle_docs_audio(message):
    pass

@bot.message_handler(regexp = 'SOME_REGEXP')
def handle_message(message):
    pass

@bot.message_handler(func = lambda message: message.document.mime_type == 'text/plain', content_types = ['documents'])
def handle_text_doc(message):
    pass

def test_message(message):
    return message.document.mime_type == 'text/plain'

@bot.message_handler(func = test_message, content_types = ['document'])
def handle_text_doc(message):
    pass

@bot.message_handler(commands=['hello'])
@bot.message_handler(func = lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def say_something(message):
    pass

@bot.message_handler(commands = ['help'])
