from datetime import datetime, timedelta
from json import dumps

from flask import Flask, render_template, redirect, session,\
url_for, request

from models import db, Link
from app import app

@app.route('/')
def index():
    end_dt = (datetime.now() + timedelta(1)).strftime("%Y-%m-%d")
    start_dt = datetime.now().strftime("%Y-%m-%d")
    user_name = session.get('user_name', None)
    template_data = {
        'user_name': user_name,
        #'entry_list': Link.query.filter(Link.dt.between(start_dt, end_dt)).all()
        'entry_list': Link.query.filter().order_by(Link.dt.desc()).limit(30).all()
    }
    return render_template('index.html', **template_data)

@app.route('/add/', methods=['POST'])
def add():
    link = request.form.get('link', None)
    body = request.form.get('body', None)
    if not session['user_name']:
        return dumps({'status': 'need auth'})
    if link is None:
        return dumps({'status': 'need data', 'field': 'link'})
    if body is None:
        return dumps({'status': 'need data', 'field': 'body'})
    if not _is_valid_url(link):
        return dumps({'status': 'not valid url', 'field': 'link'})

    link = Link(link, body, session['user_name'])
    db.session.add(link)
    db.session.commit()

    return dumps({'status': 'ok'})


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def _is_valid_url(url):
    import re
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None
