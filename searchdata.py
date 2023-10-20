import json


def get_outgoing_links(URL):
    fhand = open("urlData.txt")
    urlData = json.load(fhand)
    if URL in urlData:
        return urlData[URL].get("outgoingLinks")
    return None


def get_incoming_links(URL):
    fhand = open("urlData.txt")
    urlData = json.load(fhand)
    if URL in urlData:
        return urlData[URL].get("incomingLinks")
    return None


def get_page_rank(URL):
    fhand = open("urlData.txt")
    urlData = json.load(fhand)
    if URL in urlData:
        return urlData[URL].get("pagerank")
    return -1


def get_idf(word):
    fhand = open("inverseDf.txt")
    inverseDf = json.load(fhand)
    if word in inverseDf:
        return inverseDf[word]
    return 0


def get_tf(URL, word):
    fhand = open("urlData.txt")
    urlData = json.load(fhand)
    if URL in urlData:
        if word in urlData[URL]["tf"]:
            return urlData[URL]["tf"][word]
    return 0


def get_tf_idf(URL, word):
    fhand = open("urlData.txt")
    urlData = json.load(fhand)
    if URL in urlData:
        if word in urlData[URL]["tfidf"]:
            return urlData[URL]["tfidf"][word]
    return 0
