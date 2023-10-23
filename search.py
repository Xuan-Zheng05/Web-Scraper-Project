import json
import math


class Document:
    def __init__(self):
        self.url = ""
        self.name = ""
        self.score = -1

    def toDictionary(self):
        selfDict = dict()
        selfDict["url"] = self.url
        selfDict["title"] = self.name
        selfDict["score"] = self.score
        return selfDict


tfidfSearch = dict()
allDocuments = []


def search(phrase, boost):
    global tfidfSearch
    tfidfSearch = dict()
    fhand = open("inverseDf.txt")
    inverseDf = json.load(fhand)
    fhand = open("urlData.txt")
    urlData = json.load(fhand)

    words = phrase.split()
    wordLen = len(words)
    query = dict()

    for word in words:
        if word in query:
            query[word] = query[word] + 1
        else:
            query[word] = 1

    tfidfQuery(query, wordLen, inverseDf)
    topTen = []
    n = 10
    for url in urlData:
        if cosineDenom(urlData[url]) > 0:
            a = cosineNum(urlData[url])
            b = cosineDenom(urlData[url])
            contentScore = a / b
        else:
            contentScore = 0

        if boost:
            contentScore = contentScore * urlData[url].get("pagerank")

        currDoc = Document()
        currDoc.url = url
        currDoc.name = urlData[url]["name"]
        currDoc.score = contentScore

        if len(topTen) == n - 1:
            topTen.append(currDoc)
            topTen = sorted(topTen, key=lambda doc: doc.score, reverse=True)
        elif len(topTen) < n - 1:
            topTen.append(currDoc)
        else:
            if currDoc.score > topTen[n - 1].score:
                topTen.pop()
                found = False
                for i in range(len(topTen)):
                    if topTen[i].score < currDoc.score:
                        topTen.insert(i, currDoc)
                        found = True
                        break
                if found != True:
                    topTen.append(currDoc)

    if len(topTen) < n:
        topTen = sorted(topTen, key=lambda doc: doc.score, reverse=True)

    for i in range(len(topTen)):
        topTen[i] = topTen[i].toDictionary()

    return topTen


def tfidfQuery(query, length, inverseDf):
    for word in query:
        tf = query[word] / length
        if word in inverseDf:
            tfidf = math.log(1 + tf, 2) * inverseDf[word]
            tfidfSearch[word] = tfidf
        else:
            tfidfSearch[word] = 0


def cosineNum(url):
    numerator = 0
    for word in tfidfSearch:
        if word in url["tfidf"]:
            numerator += tfidfSearch[word] * url["tfidf"][word]

    return numerator


def cosineDenom(url):
    query = 0
    doc = 0
    for word in tfidfSearch:
        query += pow(tfidfSearch[word], 2)
        if word in url["tfidf"]:
            doc += pow(url["tfidf"][word], 2)

    denominator = math.sqrt(query) * math.sqrt(doc)
    return denominator
