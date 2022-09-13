#! /usr/local/bin/python3.10

import json

with open('json.json', 'r') as json_file:
    data = json.load(json_file)

print(data)

print(json.dumps(data))

print(json.dumps(data, indent=1))

print(data[0]['name'] + ' ' + data[0]['location'] + ' ' + str(data[0]['followers']), data[1]['name'] + ' ' + data[1]['location'] + ' ' + str(data[1]['followers']))
print(data[0]['name'], data[0]['location']) 
print(data[1]['name'], data[1]['location'])
