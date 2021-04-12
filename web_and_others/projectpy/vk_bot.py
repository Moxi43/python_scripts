###UTF-8###
###UTF-8### ### ДОПИСАТЬ ПРИЕМ ГОРОДА ДЛЯ ПОГОДЫ С ПОМОЩЬЮ ФАЙЛА

###UTF-8###
import requests
import bs4
import datetime
import json

class VkBot:
    def __init__(self, user_id):
        print('Создан объект бота!')
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._COMMANDS = ['ПРИВЕТ', 'ПОГОДА', 'ВРЕМЯ', 'ПОКА']

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get('https://vk.com/id'+str(user_id))
        bs = bs4.BeautifulSoup(request.text, 'html.parser')

        user_name = self._clean_all_tag_from_str(bs.findAll('title')[0])

        return user_name.split()[0]

    #Достаем время
    def _get_time(self):
        request = datetime.datetime.now()
        return self._clean_all_tag_from_str(str(request))

    #Достаем погоду
    def _get_weather(self):
        #Обращение к тексту по url.
        f = open('C:/python/projectpy/text.txt', 'r')
        f2 = f.read()
        f.close()

        city = str(f2)
        self.url = "https://api.openweathermap.org/data/2.5/weather?q="+str(f2)+",ru&appid=b7a85bb343e46c199875c344c5a8674e"
        url = self.url
        #Занесение информации, полученной из url в переменную k в формате JSON
        self.response = requests.request("GET", url)
        response = self.response
        self.k = response.json()
        k = self.k

        #Проверка команд и вынесение информации

        if k["coord"] != "404":
            city = k["name"]
            sky = k["main"]
            speed = k["wind"]["speed"]
            temp = k["main"]["temp"]

        self.wind_speed = "Скорость ветра: " + str(speed) + " метров в секунду. &#127788;\n"
        ws = self.wind_speed 

        tmp = "Температура за окном: " + str(round(int(temp) - 273.15)) + "C°. &#127770; \n "
     
        if sky == "Clear":
            return "Небо чистое! " + ws + tmp + "Указанный город: " + str(city) 
            
        else:
            return "Облачно. &#9729;\n " + ws + tmp + "Указанный город:" + str(city) 
        #

    #Метод очистки ненужных тегов и прочего мусора
    @staticmethod 
    def _clean_all_tag_from_str(string_line):
        ''' Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка''' 
        result = ''
        not_skip = True 
        for i in list(string_line):
            if not_skip:
                if i == '<':
                    not_skip = False
                else:
                    result += i
            else:
                if i == '>':
                    not_skip = True 
        return result          

    #Указание логики для команд             

    def new_message(self, message):
        if message.upper() == self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}!"
    
    # Погода
        elif message.upper() == self._COMMANDS[1]:
            return self._get_weather()
    # Время
        elif message.upper() == self._COMMANDS[2]:
            return self._get_time()
    
    # Пока
        elif message.upper() == self._COMMANDS[3]:
            return f"Пока-пока, {self._USERNAME}!"
    
        else:
            return "Не понимаю о чем вы..."

    