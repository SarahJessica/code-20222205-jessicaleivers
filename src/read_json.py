import json


def from_file(path='../data.json'):
    with open(path) as data:
        d = json.load(data)
        data.close()
    print(d)
