from flask import session
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView

from models import Link, db
from config import params
from app import app

class MyView(ModelView):
    def is_accessible(self):
        full_name = session.get('full_name', None)
        return full_name == params.ADMIN

admin = Admin(app)
admin.add_view(MyView(Link, db.session))