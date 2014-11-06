#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    User model
    ~~~~~~~~~~

    The user model.

    This is to be used with Flask-User. It's a good example of a simple ORM in
    Flask.

    :author: Jeff Kereakoglow
    :date: 2014-11-05
    :copyright: (c) 2014 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
from flask_user import UserMixin
from app import db

# Define the User data model. Make sure to add flask.ext.user UserMixin !!!
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    # User authentication information
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    reset_password_token = db.Column(db.String(100), nullable=False, server_default='')

    # User email information
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())

    # User information
    is_enabled = db.Column(db.Boolean(), nullable=False, server_default='0')
    first_name = db.Column(db.String(100), nullable=False, server_default='')
    last_name = db.Column(db.String(100), nullable=False, server_default='')

    def is_active(self):
        return self.is_enabled
