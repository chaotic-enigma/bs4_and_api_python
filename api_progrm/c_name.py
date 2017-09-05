import json
import urllib2

def get_weather_details():
	
	name = raw_input('Enter the city name: ')
	
	weather_api = '9d41bd4e5bffd04e03a6cb6832066559'

	weather_url = 'http://api.openweathermap.org/data/2.5/weather?q='+name+'&appid='+weather_api

	w_open_url = urllib2.urlopen(weather_url)

	json_open_w = json.load(w_open_url)
	print
	temperature = json_open_w['main']['temp']
	celsius = temperature - 273
	farenheit = celsius * 9/5 + 32
	try:
		print '#################################################'
		print
		print '\tRegion: %s' %json_open_w['name']
		print '\tWeather Description: %s' %json_open_w['weather'][0]['description']
		print '\tTemperature in Celsius: %s C' %celsius
		print '\tTemperature in Farenheit: %s F' %farenheit
		print '\tHumidity: %s' %json_open_w['main']['humidity']
		print '\tWind Speed: %s mph' %json_open_w['wind']['speed']
		print '\tPressure: %s pascals' %json_open_w['main']['pressure']
		print '\tTotal Clouds: %s' %json_open_w['clouds']['all']
		print '\tCountry: %s' %json_open_w['sys']['country']
		print
		print '#################################################'
		print
	except KeyError:
		print
		print('\tWARNING \n\tsomething wrong with the deatils of the location')
		print
	return None
	
get_weather_details()

