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
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config.from_object("config")

cache = SimpleCache(__name__)

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

db = SQLAlchemy(app)
db.create_all() # Must be called AFTER all model files are imported

#-- Models
from app.models import user

#-- Flask User init
db_adapter = SQLAlchemyAdapter(db, user)
user_manager = UserManager(db_adapter, app)

#-- Controllers
from app.controllers import public
from app.controllers import private

app.register_blueprint(public.mod)
app.register_blueprint(private.mod)
