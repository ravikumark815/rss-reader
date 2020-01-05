import feedparser
from pprint import pprint

def parse(url):
    return feedparser.parse(url)

def getMeta(parsedData):
    feed = parsedData['feed']
    return {
        'link': feed['link'],
        'title': feed['title'],
        'subtitle': feed['subtitle']
    }

def getFeeds(parsedData):
    feeds = []    
    entries = parsedData['entries']
    for i in entries:
        feeds.append({
            'id': i['id'],
            'title': i['title'],
            'summary': i['summary'],
            'link': i['link'],
            'published': i['published_parsed'],
        })
    return feeds