#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Private controller
    ~~~~~~~~~~~~~~~
    The private controller.

    All public pages of the application ought to be controlled through this
    file.

    :author: Jeff Kereakoglow
    :date: 2014-11-06
    :copyright: (c) 2014 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
from flask import Blueprint, render_template
from app.utils import cache_data, fetch_cached_data
from flask_user import current_user, login_required

mod = Blueprint("private", __name__)
args = {"title":'',
        "stylesheet":'',
        "active_page":'',
        "show_header":True}

@mod.route('/dashboard', methods=["GET"])
@login_required
def dashboard():
    """
    Renders the view for the home controller.

    :returns: HTML
    :rtype: flask.Response
    """

    args["title"] = "Dashboard"
    args["active_page"] = "dashboard"
    args["stylesheet"] = "dashboard"
    args["show_header"] = "private"

    # Prevent caching if in debug mode.
    return render_template("private/dashboard.html", args=args)

    # # Check for a cached response
    # rv = fetch_cached_data()
    #
    # if rv is not None:
    #     return rv
    #
    # out = render_template("home.html", args=args)
    #
    # # Automatically cached for 15 minutes
    # cache_data(out)
    #
    # return out

@mod.route('/profile', methods=["GET"])
@login_required
def profile():
    """
    Renders the view for the home controller.

    :returns: HTML
    :rtype: flask.Response
    """
    # Prevent caching if in debug mode.
    return render_template("private/profile.html", title="Profile")
