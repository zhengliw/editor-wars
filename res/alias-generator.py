import json
import yaml
import sys

with open(sys.argv[1]) as yaml_stream:
    source_yaml = yaml.safe_load(yaml_stream)

obj = set()

for editor,value in source_yaml.items():
    name = value['name'].lower()
    tag = editor.lower()

    obj.add((name, tag))
    obj.add((tag, tag))

    parts = [ part for part in name.split() ]
    for part in parts:
        obj.add((part, tag))

obj = list(obj)

print(sorted(obj, key=lambda x: x[0]))

json_obj = {}

json_obj["alias"] = [pair[0] for pair in obj]
json_obj["id"] = [pair[1] for pair in obj]

with open(sys.argv[2], "w") as json_stream:
    json.dump(json_obj, json_stream)



