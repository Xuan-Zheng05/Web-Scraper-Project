import webdev
import math
import json
import os


# class that converts url data to json
class UrlDataEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


# class that stores all necessary information for a url
class urlData:
    def __init__(self):
        self.name = ""
        self.content = dict()
        self.outgoingLinks = []
        self.incomingLinks = []
        self.numWords = 0
        self.pagerank = -1
        self.tf = dict()
        self.tfidf = dict()
        self.pos = -1


inverseDF = dict()
urlQueue = []
urlUsed = set()
allUrlData = dict()
urlList = []
pageRankResult = []


def crawl(seed):
    # deletes the data from previous crawl
    open("urlData.txt", "w")
    open("inverseDf.txt", "w")

    # adds seed as first URL
    urlQueue.append(seed)
    urlUsed.add(seed)

    pos = 0
    while len(urlQueue) > 0:
        currUrl = urlQueue[0]
        urlQueue.pop(0)

        contents = webdev.read_url(currUrl)

        # checks if the current url has already been initalized as an object
        if currUrl in allUrlData:
            currUrlData = allUrlData[currUrl]
        else:
            currUrlData = urlData()

        currUrlData.pos = pos
        urlList.append(currUrl)
        pos += 1
        # gets the name for the current URL
        titleIndex = contents.index("<title>")
        titleEnd = contents.index("</title>")
        title = contents[titleIndex + 7 : titleEnd]
        currUrlData.name = title

        # gets all words from the current URL and organizes them into a dictionary
        words = dict()
        startP = [i for i in range(len(contents)) if contents.startswith("<p>", i)]
        endP = [i for i in range(len(contents)) if contents.startswith("</p>", i)]
        for i in range(len(startP)):
            allWords = contents[startP[i] + 4 : endP[i]]
            wordList = allWords.split()
            for word in wordList:
                if word not in words:
                    words[word] = 1
                else:
                    words[word] = words[word] + 1

            # records number of words in document for later use
            currUrlData.numWords = currUrlData.numWords + len(wordList)

        currUrlData.content = words

        # gets all links from the current URL and adds them to the queue
        # furthermore also finds outgoing and incoming links
        outgoingLinks = []
        delUrlIndex = currUrl.rindex("/")
        blankUrl = currUrl[:delUrlIndex]
        instances = [i for i in range(len(contents)) if contents.startswith("href=", i)]
        for index in instances:
            url = ""
            i = index + 6
            while contents[i] != '"':
                url += contents[i]
                i += 1
            if url[0] == ".":
                url = blankUrl + url[1:]

            if url not in urlUsed:
                urlQueue.append(url)

            # code for incomign URLs
            if currUrl != url:
                if url in allUrlData:
                    incomingUrl = allUrlData[url]
                else:
                    incomingUrl = urlData()
                incomingUrl.incomingLinks.append(currUrl)
                allUrlData[url] = incomingUrl
            urlUsed.add(url)

            # this is for outgoing URLs
            outgoingLinks.append(url)

        currUrlData.outgoingLinks = outgoingLinks
        allUrlData[currUrl] = currUrlData

    # after crawling through all documents, calculate the tf, idf, tfidf, and PageRank
    calculateTf()
    calculateIdf()
    calculateTfidf()
    calculatePageRank()

    # stores the data of urlData and inverseDf into files
    urlJson = UrlDataEncoder().encode(allUrlData)
    open("urlData.txt", "w").write(urlJson)
    urlJson = UrlDataEncoder().encode(inverseDF)
    open("inverseDf.txt", "w").write(urlJson)

    return len(urlUsed)


# function that calculates the term frequency for each word in each document
# no output or input
def calculateTf():
    for url in urlUsed:
        currUrl = allUrlData[url]
        content = currUrl.content
        for word in content:
            currUrl.tf[word] = content[word] / currUrl.numWords

            # calculating how many documents a word appears in
            if word not in inverseDF:
                inverseDF[word] = 1
            else:
                inverseDF[word] = inverseDF[word] + 1

        allUrlData[url] = currUrl


# function that calculates the idf for each word
# no output or input
def calculateIdf():
    for word in inverseDF:
        inverseDF[word] = math.log(len(urlUsed) / (1 + inverseDF[word]), 2)


# function that calculates the tfidf for each word in a document
# no output or input
def calculateTfidf():
    for url in urlUsed:
        currUrl = allUrlData[url]
        for word in currUrl.tf:
            currUrl.tfidf[word] = math.log(1 + currUrl.tf[word], 2) * inverseDF[word]

        allUrlData[url] = currUrl


# function for calculating the PageRank
# no output or input
def calculatePageRank():
    # generates the probability matrix
    matrix = [[0 for _ in range(len(urlList))] for _ in range(len(urlList))]
    for url in urlList:
        currUrl = allUrlData[url]
        for outgoing in currUrl.outgoingLinks:
            outUrl = allUrlData[outgoing]
            index = outUrl.pos

            matrix[currUrl.pos][outUrl.pos] = 1
        numOnes = len(currUrl.outgoingLinks)
        for j in range(len(matrix[currUrl.pos])):
            matrix[currUrl.pos][j] = float(matrix[currUrl.pos][j]) / numOnes
            matrix[currUrl.pos][j] = matrix[currUrl.pos][j] * (1 - 0.1)
            matrix[currUrl.pos][j] = matrix[currUrl.pos][j] + 0.1 / len(urlList)

    t0 = [[0.1 for _ in range(len(urlList))] for _ in range(1)]
    result = [[0 for _ in range(len(urlList))] for _ in range(1)]
    for i in range(len(result)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix)):
                result[i][j] += t0[i][k] * matrix[k][j]

    t0 = result
    dis = 1
    while dis > 0.0001:
        result = [[0 for _ in range(len(urlList))] for _ in range(1)]
        for i in range(len(result)):
            for j in range(len(matrix[0])):
                for k in range(len(matrix)):
                    result[i][j] += t0[i][k] * matrix[k][j]

        sum = 0
        for i in range(len(result[0])):
            sum += pow(result[0][i] - t0[0][i], 2)
        dis = math.sqrt(sum)
        t0 = result

    for i in range(len(result[0])):
        pageRankResult.append(result[0][i])
    for url in urlList:
        currUrl = allUrlData[url]
        currUrl.pagerank = pageRankResult[currUrl.pos]
        allUrlData[url] = currUrl
    return matrix


crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html")
print()
