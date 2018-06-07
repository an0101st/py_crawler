import crawler

fetcher = crawler.ArticleFetcher()

for e in fetcher.fetch():
    print(e.emoji + ": " + e.title)