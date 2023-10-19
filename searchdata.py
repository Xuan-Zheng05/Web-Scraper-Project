import json

fhand = open("urlData.txt")
urlData = json.load(fhand)
fhand = open("inverseDf.txt")
inverseDf = json.load(fhand)


def get_outgoing_links(URL):
    if URL in urlData:
        return urlData[URL].get("outgoingLinks")
    return None


def get_incoming_links(URL):
    if URL in urlData:
        return urlData[URL].get("incomingLinks")
    return None


def get_page_rank(URL):
    return -1


def get_idf(word):
    if word in inverseDf:
        return inverseDf[word]
    return 0


def get_tf(URL, word):
    if URL in urlData:
        if word in urlData[URL]["tf"]:
            return urlData[URL]["tf"][word]
    return 0


def get_tf_idf(URL, word):
    if URL in urlData:
        if word in urlData[URL]["tfidf"]:
            return urlData[URL]["tfidf"][word]
    return None
