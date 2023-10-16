import webdev
import os

urlQueue = []
urlUsed = set()


def crawl(seed):
    contents = webdev.read_url(seed)

    delUrlIndex = seed.rindex("/")
    blankUrl = seed[:delUrlIndex]

    res = [i for i in range(len(contents)) if contents.startswith("href=", i)]
    for index in res:
        url = ""
        i = index + 6
        while contents[i] != '"':
            url += contents[i]
            i += 1
        if url[0] == ".":
            url = blankUrl + url[1:]
        if url not in urlUsed:
            urlUsed.add(url)
            crawl(url)


crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html")
print()
