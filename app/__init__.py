#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Application
    ~~~~~~~~~~~

    The Flask application module.

    :author: Jeff Kereakoglow
    :date: 2014-11-05
    :copyright: (c) 2014 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
from flask import Flask, render_template, abort
from werkzeug.contrib.cache import SimpleCache
from flask_sqlalchemy import SQLAlchemy
from flask_user import SQLAlchemyAdapter, UserManager

# Initialize the app and the ORM
app = Flask(__name__)
cache = SimpleCache(__name__)
db = SQLAlchemy(app)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config.from_object("config")

#-- Models
from app.models import user

#-- Flask User init
db_adapter = SQLAlchemyAdapter(db, user.User, UserAuthClass=user.UserAuth)
user_manager = UserManager(db_adapter, app)

db.create_all()
# Seed database
#           username, first_name, last_name, email, password
user.create("hsimpson", "Homer", "Simpson", "homer@simpsons.com", "doh")

db.session.commit()

#-- Controllers
from app.controllers import public
from app.controllers import private

app.register_blueprint(public.mod)
app.register_blueprint(private.mod)

@app.errorhandler(403)
def not_found(error):
    """
    Renders 403 page

    :returns: HTML
    :rtype: flask.Response
    """
    return render_template("404.html", title="403"), 403

@app.errorhandler(404)
def not_found(error):
    """
    Renders 404 page

    :returns: HTML
    :rtype: flask.Response
    """
    return render_template("404.html", title="404"), 404
