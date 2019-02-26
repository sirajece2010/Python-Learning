import json, os

#data = json.loads(os.environ)

data = dict(os.environ)

print(data.keys())