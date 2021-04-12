import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz 
import pyttsx3
import datetime

opts = {
	"alias": ("измаил", "изм", "маил", "измаилушка", "змаил", "маилушка"),
	"tbr": ("скажи", "расскажи", "покажи", "сколько", "произнеси"),
	"cmds": {
		"ctime": ("текущее время", "сколько время", "который час"),
		"radio": ("включи музыку", "включи радио", "воспроизведи радио", "воспроизведи музыку"),
		"browser": ("включи браузер", "открой браузер", "запусти браузер", "открой гугл"),
		"stupid1": ("расскажи анекдот", "пошути","расскажи шутку", "рассмеши меня", "ты знаешь анекдоты")
		}
}		

#functions  
def speak(what):
	print(what)
	speak_engine.say(what)
	speak_engine.runAndWait()
	speak_engine.stop()

def callback(recognizer, audio):
	try:
		voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
		print("[log] Распознано: " + voice)

		if voice.startswith(opts["alias"]):
		#Appeal to Ismail
			cmd = voice 

			for x in opts['alias']:
				cmd = cmd.replace(x, "").strip() 

			for x in opts['tbr']:
				cmd = cmd.replace(x, "").strip()

		#recognize and execute commands

			cmd = recognize_cmd(cmd)		
			execute_cmd(cmd['cmd'])

			

	except sr.UnknownValueError:
		print("[log] Голос не распознан!")

	except sr.RequestError as e:
		print("[log] Неизвестная ошибка. Проверьте интернет-соединение!")



def recognize_cmd(cmd):
	RC = {'cmd': '', 'percent': 0}
	for c,v in opts['cmds'].items():
		for x in v:
			vrt = fuzz.ratio(cmd, x)
			if vrt > RC['percent']:
				RC['cmd'] = c
				RC['percent'] = vrt
	return RC			

def execute_cmd(cmd):
	if cmd == 'ctime':
		#say current time
		now = datetime.datetime.now()
		speak("Сейчас " + str(now.hour) + ':' + str(now.minute))	

	elif cmd == "radio":
		#turnON radio
		os.system("C:\\python\\Keshahelp\\radio_record.m3u")

	elif cmd == "stupid1":
		speak("Прости, но анекдотов я не знаю...")

	elif cmd == "browser":
		os.system("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")	

	else:
		speak("Команда не распознана, попробуйте повторить!")
#launch sound helper

r = sr.Recognizer()
m = sr.Microphone(device_index = 1)

with m as source:
	r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)

speak("Доброго времени суток!")
speak("Чем могу быть полезен?")

stop_listening = r.listen_in_background(m, callback)
while True:
	time.sleep(0.1)