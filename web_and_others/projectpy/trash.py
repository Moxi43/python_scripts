
import requests
import bs4
import datetime
import json
def _get_weather(self):
        #Обращение к тексту по url.
        self.url = "https://api.openweathermap.org/data/2.5/weather?q=Sarapul,ru&appid=b7a85bb343e46c199875c344c5a8674e"
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