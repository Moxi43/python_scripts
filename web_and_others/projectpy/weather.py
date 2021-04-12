import vk_api
import requests
import bs4
import datetime
import json
from vk_bot import VkBot
from vk_api.longpoll import VkLongPoll, VkEventType 

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 123456})
# API-ключ созданный ранее
token = "1467bfa5e480b7bf9a4ef1e157282bce2851766c7ea36dcf6f4a8a5d82c66e5551beeb6560cdecb939fcb"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл 
print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by:  {event.user_id} ', end='')
            
            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))
            
            print('Text: ', event.text); textik = event.text
            