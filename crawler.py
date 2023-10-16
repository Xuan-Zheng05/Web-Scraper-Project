import webdev
import os


# class that stores all nessecary information for a url
class urlData:
    name = ""
    content = dict()
    outgoingLinks = []
    incomingLinks = set()


urlUsed = set()
allUrlData = dict()


def crawl(seed):
    # TODO delete all stuff before the crawl

    contents = webdev.read_url(seed)

    # checks if the current url has already been initalized as an object
    if seed in allUrlData:
        currUrlData = allUrlData[seed]
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
    currUrlData.content = words

    # gets all links from the current URL and also crawls through them
    # furthermore also finds outgoing and incoming links
    outgoingLinks = []
    delUrlIndex = seed.rindex("/")
    blankUrl = seed[:delUrlIndex]
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
            urlUsed.add(url)
            if seed != url:
                if url in allUrlData:
                    incomingUrl = allUrlData[url]
                else:
                    incomingUrl = urlData()
                incomingUrl.incomingLinks.add(seed)
                allUrlData[url] = incomingUrl

            crawl(url)

        # this is for outgoing and incoming URLs
        outgoingLinks.append(url)

    currUrlData.outgoingLinks = outgoingLinks
    allUrlData[seed] = currUrlData
    return len(urlUsed)


crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html")
print()
