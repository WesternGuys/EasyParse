import json
from depthObject import depthObject
from masterJSON import masterJSON

def jsonProcess(fileName):
    with open(fileName) as jsonFile:
        master = json.load(jsonFile)

    print(master)

def main():
    name = input("Json File name: ")
    jsonProcess(name)

main()
