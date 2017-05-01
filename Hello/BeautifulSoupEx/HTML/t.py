import feedparser

url = "http://rss.ohmynews.com/rss/top.xml"
news = feedparser.parse(url)

print(news[ "url" ])
print(news[ "version" ])
print(news[ "channel" ][ "title" ] )
print(news[ "channel" ][ "description" ] )
print(news[ "channel" ][ "link" ] )
print(news[ "channel" ][ "copyright" ] )
print('='*100)

print(news['feed']['title'])
print(news['feed']['link'])
print(news['feed']['copyright'])
print(news.headers)
print(news.headers.get('Date'))
print(news.version)
print(len(news['entries']))
print(news['entries'][0]['title'] )
print(news.entries[0]['link']  )
print('='*100)
print(len(news['items']))
items = news['items']
for item in items:
    print(item[ "link" ],item[ "title" ] )