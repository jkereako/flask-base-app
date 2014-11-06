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

app = Flask(__name__)
app.config.from_object("config")
cache = SimpleCache(__name__)

#-- Flask extentions
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    """
    Renders 404 page

    :returns: HTML
    :rtype: flask.Response
    """
    return render_template("404.html"), 404


#-- Models
from app.models import user

db.create_all() # Must be called AFTER all model files are imported

#-- Flask User init
db_adapter = SQLAlchemyAdapter(db, user)
user_manager = UserManager(db_adapter, app)

#-- Controllers
from app.controllers import home
# from app.controllers import posts

app.register_blueprint(home.mod)
# app.register_blueprint(posts.mod)
