import json, os

#data = json.loads(os.environ)

data = dict(os.environ)

print(data.keys())

'''for root, dirname, fname in os.walk(os.getcwd()):
    print (type(fname))'''