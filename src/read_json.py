import json


def from_file(path):
    with open(path) as data:
        d = json.load(data)
        data.close()

    return d
