Flig
=============

Flig is a fast and easy linkblog written on Python with Flask and friends

Install
------------

### Just follow these steps

Create new virtual env:

    mkdir flig_env
    cd test_env/
    virtualenv .

Clone project from GitHub:

    git clone git@github.com:allaud/Flig.git

Install dependencies:

    bin/pip install -r Flig/deploy/requirements.txt

Fix default flask-oauth bug by fetching fresh version:

    bin/pip uninstall flask-oauth
    bin/pip install git+git://github.com/mitsuhiko/flask-oauth.git

Create database:

    bin/python
    >>> from Flig.models import db
    >>> db.create_all()
    >>> quit()

Let SQLite to make changes in db file:

    chmod -R o+w Flig/db

Run project:

    bin/python Flig/run.py 

Of course, you can add your own keys into config/params.py