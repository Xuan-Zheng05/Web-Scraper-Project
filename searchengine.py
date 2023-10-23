import crawler
import search

print("Which url would you like to search from?")
url = input()
crawler.crawl(url)

contin = True
while contin:
    print("Enter your search terms seperated by a space")
    searchWords = input()

    print("Would you like to boost using PageRank? (Yes or No)")
    if input() == "Yes":
        boost = True
    else:
        boost = False

    topTen = search.search(searchWords, boost)

    for i in range(len(topTen)):
        doc = topTen[i]
        print("Url:", doc["url"], "Title:", doc["title"], "Score:", doc["score"])

    print("Would you like to search for more terms? (Yes or No)")
    if input() == "No":
        contin = False
