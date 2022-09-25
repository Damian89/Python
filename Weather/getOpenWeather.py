# getOpenWeather.py: Prints the weather for a location from the command line.
# from the Open Weather Map API
# my appid is '6fc59ea854f7f40a294fe43f7012be2c'

import json
import requests
import sys

# Compute location from command line arguments.

if len(sys.argv) < 2:
    #print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    print('Usage: getOpenWeather.py Latitude, Longitude')
    sys.exit()

lat = float(sys.argv[1])
lon = float(sys.argv[2])

#location = ' '.join(sys.argv[1:])

#lat = float(input('enter Latitude:  '))
#lon = float(input('enter Longitude:  '))



# Download the JSON data from OpenWeatherMap.org's API.

#url = 'https://api.openweathermap.org/data/2.5/forecast?lat=42.2917&lon=-85.5872&cnt=40&appid=6fc59ea854f7f40a294fe43f7012be2c'
url = 'https://api.openweathermap.org/data/2.5/forecast?lat=%f&lon=%f&cnt=40&appid=6fc59ea854f7f40a294fe43f7012be2c' % (lat, lon)

response = requests.get(url)
response.raise_for_status() # checks that the request is successful

# Uncomment to see the raw JSON text:
# print(response.text)

# Load JSON data into a Python variable.

weatherData = json.loads(response.text)

# Print weather conditions. You need to look at the structure of the json file to determine the location of the necessary information. Reading it with jless helps.
c = weatherData['city']
print('----------------------------------------------------')
print('Weather for', str(c['name'])+',', str(c['country']) + ':')
print('----------------------------------------------------')
w = weatherData['list']
# Convert current temperature to Fahrenheit
currentTemp = ((w[0]['main']['temp'])-273.15)*(9/5)+32
roundedTemp = round(currentTemp,2)
print('Current temperature:', str(roundedTemp), 'degrees F')
# Print weather descriptions
print('Current conditions:', w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('Tomorrow:', w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('Day after tomorrow:', w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print('Three days from today:', w[3]['weather'][0]['main'], '-', w[3]['weather'][0]['description'])
print('----------------------------------------------------')
print('Have a nice day!')
print('----------------------------------------------------')
