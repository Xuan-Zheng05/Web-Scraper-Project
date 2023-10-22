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

    if phrase == "tomato banana blueberry blueberry":
        print()
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
        if url == "http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html":
            print()
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


# search("banana apple pear coconut apple apple", False)
# print()

# Failed Test #302 checking search results for 'banana apple pear coconut apple apple' and boost = False

# expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 0.9979087300308276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 0.9923639821311339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9897326068347375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html', 'title': 'N-172', 'score': 0.9891998801191023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-795.html', 'title': 'N-795', 'score': 0.9888294826380608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9881447489757941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9873445503442467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-305.html', 'title': 'N-305', 'score': 0.9865419172826172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-556.html', 'title': 'N-556', 'score': 0.9843796050986671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9838795503055123}]
# result = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 0.9979087300308276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 0.9923639821311339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9897326068347374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html', 'title': 'N-172', 'score': 0.989199880119102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-795.html', 'title': 'N-795', 'score': 0.9888294826380608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9881447489757941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9873445503442467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-305.html', 'title': 'N-305', 'score': 0.9865419172826173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-556.html', 'title': 'N-556', 'score': 0.984379605098667}]


# Failed Test #334 checking search results for 'peach pear apple tomato apple apple tomato' and boost = False

# expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9999957846057485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 0.9997550911156046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9996668466785874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9987854110989463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html', 'title': 'N-781', 'score': 0.9980792489481389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 0.9978369231293158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 0.9966218934019153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.996384977729776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html', 'title': 'N-74', 'score': 0.9960542431570496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-663.html', 'title': 'N-663', 'score': 0.9958611178813179}]
# result = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9999957846057483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 0.9997550911156047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9996668466785874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9987854110989461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html', 'title': 'N-781', 'score': 0.9980792489481389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 0.9978369231293158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 0.9966218934019153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9963849777297757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html', 'title': 'N-74', 'score': 0.9960542431570497}]


# Failed Test #373 checking search results for 'peach apple apple apple pear tomato' and boost = False

# expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9999945342732718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 0.9995983884868404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9994872917882923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9989393514240835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html', 'title': 'N-781', 'score': 0.9984447037019377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 0.9974094630704675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 0.9969069844919712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9968419415692983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html', 'title': 'N-74', 'score': 0.996476683548252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-663.html', 'title': 'N-663', 'score': 0.9960056358567778}]
# result = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9999945342732716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 0.9995983884868404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9994872917882921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9989393514240833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html', 'title': 'N-781', 'score': 0.9984447037019373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 0.9974094630704676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 0.996906984491971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9968419415692978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html', 'title': 'N-74', 'score': 0.9964766835482519}]


# Failed Test #380 checking search results for 'tomato coconut peach coconut banana pear coconut apple' and boost = False

# expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 0.9999828234269146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9992607840285794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.991938022345541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9880426172513057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9868620971341494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9861556168025143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9831656574862688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'title': 'N-937', 'score': 0.9813483683360322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9794519244483613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-750.html', 'title': 'N-750', 'score': 0.978222273661371}]
# result = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 0.9999828234269147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9992607840285795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.991938022345541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9880426172513056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9868620971341496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9861556168025144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9831656574862687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'title': 'N-937', 'score': 0.9813483683360326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9794519244483612}]
