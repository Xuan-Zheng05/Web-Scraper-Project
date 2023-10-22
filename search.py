import json
import math


class Document:
    def __init__(self):
        self.url = ""
        self.name = ""
        self.score = -1


tfidfSearch = dict()


def search(phrase, boost):
    fhand = open("inverseDf.txt")
    inverseDf = json.load(fhand)
    fhand = open("urlData.txt")
    urlData = json.load(fhand)

    words = phrase.split()
    wordLen = len(words)
    query = {word: 1 for word in words}

    tfidfQuery(query, wordLen, inverseDf)

    topTen = []
    for url in urlData:
        contentScore = cosineNum(urlData[url]) / cosineDenom(urlData[url])
        if boost:
            contentScore = contentScore * urlData[url].get("pagerank")

    result = dict()
    list = []
    return list


def tfidfQuery(query, length, inverseDf):
    for word in query:
        tf = query[word] / length
        tfidf = math.log(1 + tf, 2) * inverseDf[word]
        tfidfSearch[word] = tfidf

    return tfidfSearch


def cosineNum(url):
    numerator = 0
    for word in tfidfSearch:
        if tfidfSearch[word] > 0 and word in url["tfidf"]:
            numerator += tfidfSearch[word] * url["tfidf"][word]
    return word


def cosineDenom():
    denominator = 0

    return denominator


search("apple banana pear", False)
print()
