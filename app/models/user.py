#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    User model
    ~~~~~~~~~~

    The user model.

    This is to be used with Flask-User. It's a good example of a simple ORM in
    Flask.

    :author: Ling Thio
    :date: 2014-11-05
    :see https://github.com/lingthio/Flask-User-starter-app/blob/master/app/users/models.py
    :copyright: (c) 2014 by SolidBuilds.com
    :license: MIT, see LICENSE for more details
"""
import datetime
from flask_user import UserMixin
from app import app, db

# Define the User data model. Make sure to add the flask_user.UserMixin !!
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    # User email information (required for Flask-User)
    email = db.Column(db.String(255), nullable=False, unique=True)
    confirmed_at = db.Column(db.DateTime())

    # User information
    is_enabled = db.Column(db.Boolean(), nullable=False, server_default='0')
    first_name = db.Column(db.String(50), nullable=False, server_default='')
    last_name = db.Column(db.String(50), nullable=False, server_default='')

    # Relationships
    user_auth = db.relationship('UserAuth', uselist=False)
    roles = db.relationship('Role', secondary='user_roles',
            backref=db.backref('users', lazy='dynamic'))

    def is_active(self):
        return self.is_enabled


# Define the UserAuth data model.
class UserAuth(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))

    # User authentication information (required for Flask-User)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    reset_password_token = db.Column(db.String(100), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')

    # Relationships
    user = db.relationship('User', uselist=False)


# Define the Role data model
class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))


# Define the UserRoles association model
class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

class UserInvitation(db.Model):
    __tablename__ = 'user_invite'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    # save the user of the invitee
    invited_by_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # token used for registration page to identify user registering
    token = db.Column(db.String(100), nullable=False, server_default='')

def create(username, first_name, last_name, email, password):
    user_auth = UserAuth.query.filter(UserAuth.username == username).first()
    if not user_auth:
        user_auth = UserAuth(username=username, password=app.user_manager.hash_password(password))
        user = User(
            is_enabled=True,
            first_name=first_name,
            last_name=last_name,
            email=email,
            confirmed_at=datetime.datetime.now(),
            user_auth=user_auth
        )
        db.session.add(user_auth)
        db.session.add(user)
