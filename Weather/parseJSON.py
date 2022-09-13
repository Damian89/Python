#! /usr/local/bin/python3.10

import json

with open('weather.json') as json_file:
    data = json.load(json_file)

#for item in data:
#    if item['name'] == 'PHP':
#        print(item['website'])
#    if item['name'] == 'Java':
#        print(item['id'])

#print(data)

for item in data:
    if item['name'] == 'Overnight':
        print(item['name'])
        print(item['detailedForecast'])