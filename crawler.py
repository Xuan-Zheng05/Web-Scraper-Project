import webdev
import math
import os


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


inverseDF = dict()
urlQueue = []
urlUsed = set()
allUrlData = dict()


def crawl(seed):
    # TODO delete all stuff before the crawl

    # adds seed as first URL
    urlQueue.append(seed)
    urlUsed.add(seed)

    while len(urlQueue) > 0:
        currUrl = urlQueue[0]
        urlQueue.pop(0)

        contents = webdev.read_url(currUrl)

        # checks if the current url has already been initalized as an object
        if currUrl in allUrlData:
            currUrlData = allUrlData[currUrl]
        else:
            currUrlData = urlData()

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

    # calculating term frequencies for each word in each url
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

    # calculating the idf for each word
    for word in inverseDF:
        inverseDF[word] = math.log(len(urlUsed) / (1 + inverseDF[word]), 2)

    # finally calculating the tfidf for each word in a document
    for url in urlUsed:
        currUrl = allUrlData[url]

    return len(urlUsed)


crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html")
print()
