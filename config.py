#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Config
    ~~~~~~

    Application-wide configurations.

    You can put whatever you want here. The convention is to write configuration
    variables in upper-case.

    :see http://flask.pocoo.org/docs/config/

    :author: Jeff Kereakoglow
    :date: 2014-11-05
    :copyright: (c) 2015 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

#-- Globals
DEBUG = True
# SECRET_KEY = os.getenv("SECRET_KEY",os.urandom(24))
SECRET_KEY = "development_key"
CACHE_TIMEOUT = 60 * 60 * 15
APP_NAME = "Flask base app"

#-- SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///db.sqlite")

#-- Flask User
# @see: https://github.com/neurosnap/Flask-User/blob/master/flask_user/settings.py#L7-L105
CSRF_ENABLED = True
USER_INVITE_URL = "/invite"
USER_REGISTER_URL = "/new-user"
USER_LOGIN_URL = "/login"
USER_LOGOUT_URL = "/logout"
USER_FORGOT_PASSWORD_URL = "/forgot-passowrd"
USER_CHANGE_PASSWORD_URL = "/change-password"
USER_PROFILE_URL = "/profile"
USER_ENABLE_CHANGE_USERNAME = False
USER_APP_NAME = APP_NAME                # Used by email templates
USER_ENABLE_INVITATION = True
#USER_REQUIRE_INVITATION = True


# Endpoints are converted to URLs using url_for()
# The empty endpoint ('') will be mapped to the root URL ('/')
USER_AFTER_LOGOUT_ENDPOINT = ''

USER_LOGIN_TEMPLATE = "public/login.html"
