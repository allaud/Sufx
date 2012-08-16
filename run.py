from app import app
from views.main import index, login, logout
from views.oauth import login_twitter, login_google,\
google_authorized, twitter_authorized

import admin

if __name__ == '__main__':
    app.run(debug=True)