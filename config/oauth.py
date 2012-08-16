from flaskext.oauth import OAuth
from flask import session

import params

oauth = OAuth()
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    consumer_key=params.twitter['consumer_key'],
    consumer_secret=params.twitter['consumer_secret']
)

google = oauth.remote_app('google',
    base_url='https://www.google.com/accounts/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                        'response_type': 'code'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'},
    consumer_key=params.google['consumer_key'],
    consumer_secret=params.google['consumer_secret']
)

@twitter.tokengetter
def get_twitter_token():
    return session.get('twitter_token')

@google.tokengetter
def get_access_token():
    return session.get('access_token')