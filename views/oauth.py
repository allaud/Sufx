from urllib import urlopen
from json import loads

from flask import Flask, flash, redirect, render_template,\
request, url_for, session
from update import import_from_twitter
from config.oauth import twitter, google

from models import Link
from app import app

@app.route('/login/twitter')
def login_twitter():
    return twitter.authorize(callback=url_for('twitter_authorized',
        next=request.args.get('next') or request.referrer or None))

@app.route('/login/google')
def login_google():
    callback=url_for('google_authorized', _external=True)
    return google.authorize(callback=callback)

@app.route('/google-authorized')
@google.authorized_handler
def google_authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    session['user_name'], session['full_name'] = _get_google_username(access_token)
    return redirect(url_for('index'))

@app.route('/twitter-authorized')
@twitter.authorized_handler
def twitter_authorized(resp):
    next_url = url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['user_name'] = resp['screen_name']
    return redirect(next_url)

@app.route('/run')
def run():
    json = import_from_twitter()
    return json

def _get_google_username(access_token):
    url = "https://www.googleapis.com/oauth2/v1/userinfo?access_token=%s" % access_token
    resp = urlopen(url).read()
    json = loads(resp)
    return json["email"].split("@")[0], json["email"]

