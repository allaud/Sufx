from urllib import urlopen
from json import loads
from models import db, Link


def import_from_twitter():
    url = "https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=allaud&count=10"
    resp = urlopen(url).read()
    json = loads(resp)

    for tweet in json:
        try:
            url = tweet['entities']['urls'][0]['expanded_url']
            short_url = tweet['entities']['urls'][0]['url']
            body = tweet['text'].replace(short_url, '')
            author = tweet['user']['screen_name']
        except IndexError:
            print "no data for parse!", tweet
            continue
        if not "#push" in body:
            continue
            
        body = body.replace('#push', '')
        link = Link(url, body, author)
        db.session.add(link)
    db.session.commit()
    return resp