import pyowm

owm = pyowm.OWM('19f8ba267bb3c2f379655e89f1eeebf3')

place = input('В каком городе/стране? ')

observation = owm.weather_at_place(place)
w = observation.get_weather()
print(w)
