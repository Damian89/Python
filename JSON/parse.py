import json

json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'

parsed_json = (json.loads(json_data))
print(json.dumps(parsed_json, indent=4, sort_keys=True))
loaded_json = json.loads(json_data)
for x in loaded_json:
    print("%s: %d" % (x,loaded_json[x]))
