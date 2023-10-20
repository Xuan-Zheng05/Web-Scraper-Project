import json


def search(phrase, boost):
    fhand = open("inverseDf.txt")
    inverseDf = json.load(fhand)

    words = phrase.split()
    wordDict = {word: 1 for word in words}
    if boost:
        temp
    else:
        temp
    result = dict()
    list = []
    return list


search("apple banana pear", False)
