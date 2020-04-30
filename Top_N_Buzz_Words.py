def topNbuzzWords(toys, quotes, topToys):
    topWords = dict()
    words = list()
    for toy in toys:
        toy = toy.lower()
        for quote in quotes:
            quote = quote.lower()
            if toy in quote:
                try:
                    wordCount = topWords[toy]
                    topWords[toy] = wordCount + quote.count(toy)
                except:
                    topWords[toy] = quote.count(toy)
    topWords = sorted(topWords.items(), key=lambda topWords: topWords[1], reverse=True)
    topWords = topWords[:topToys]
    for topWord in range(len(topWords)):
        words.append(topWords[topWord][0])
    words.sort()
    return(words)

if __name__ == "__main__":
    toys = ["elsa", "elmo", "legos", "drone", "tablet", "warcraft"]
    quotes = ["Elmoa is the hottest of the season! Elmoa will be on every kid's wishlist!",
        "The new Elmoa dolls are super high quality",
        "Expect the Elsaa dolls to be very popular this year, Elsaa!",
        "Elsaa and Elmoa are the toys I'll be buying for my kids, Elsaa is good",
        "For parents of older kids, look into buying them a drone",
        "Warcraft is slowly rising in popularity ahead of the holiday season"]
    topToys = 2
    checkToys = topNbuzzWords(toys, quotes, topToys)
    print(checkToys)