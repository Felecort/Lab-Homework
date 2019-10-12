import pyowm
import time
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru") 
def Weather():
	print("Модуль определения погоды 1.4 Основан на библиотеке 'pyown'")
	print("------------------------------------")
	print('для закрытия программы введите "стоп"')
	def Weather_determinant(place):
		observation = owm.weather_at_place(place)
		w = observation.get_weather()
		temp = w.get_temperature('celsius')["temp"]
		wind = w.get_wind ()["speed"] 
		humidity = w.get_humidity ()
		print("В городе ", place, " сейчас ", w.get_detailed_status())
		print("Скорость ветра =", round(wind), "м/с")
		print("Влажность =", humidity, "%")
		print( "Температуа в районе", (round(temp)), "°C")
		if temp < -10:
			print("Холодрыга жуткая, надевай два пуховика")
		elif temp < 0:
			print("На улице холодно, одевайся теплее")
		elif temp < 10:
			print("Прохладненько, смотри не заболей")
		elif temp < 20:
			print("Не май месяц на дворе, всё таки")
		elif temp < 25:
			print("Лучшего и не пожелаешь")
		else:
			print("Словно на Мальдивах")
	j = 1
	while j != 0:
		print("------------------------------------")
		place = input("Введите название города: ")
		if place != "стоп":
			Weather_determinant(place)
		else:
			j = 0
			print ('Завершение программы через 3 секунд')
			for i in range(3,0,-1):
			    time.sleep(1)
			    print (i)
print(Weather())
raise SystemExit
