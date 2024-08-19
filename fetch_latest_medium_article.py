import feedparser

MEDIUM_USERNAME = "parameshwarbhat411"
FEED_URL = f"https://medium.com/feed/@{MEDIUM_USERNAME}"

feed = feedparser.parse(FEED_URL)
latest_article = feed.entries[0]

title = latest_article.title
link = latest_article.link

print(f"::set-output name=title::{title}")
print(f"::set-output name=link::{link}")