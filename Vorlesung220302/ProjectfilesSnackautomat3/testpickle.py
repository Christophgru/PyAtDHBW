import json

import jsonpickle


def writedata(data):
    with open('jsonpickletest.json', 'w') as outfile:
        json.dump(data, outfile)


def readdata():
    try:
        with open('jsonpickletest.json') as infile:
            return json.load(infile)
    except FileNotFoundError:
        print("Json file konnte nicht gefunden werden")
        return None


class Thing(object):
    def __init__(self, name):
        self.name = name


obj = Thing('Awesome')

frozen = jsonpickle.encode(obj)

writedata(frozen)
gelesen= readdata()


thawed = jsonpickle.decode(gelesen)
assert obj.name == thawed.name
print(thawed.name)