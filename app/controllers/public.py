#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Public controller
    ~~~~~~~~~~~~~~~
    The public controller.

    All public pages of the application ought to be controlled through this
    file.

    :author: Jeff Kereakoglow
    :date: 2014-11-05
    :copyright: (c) 2014 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
from flask import Blueprint, render_template
from app.utils import cache_data, fetch_cached_data

mod = Blueprint("public", __name__)

args = {"title":'',
        "stylesheet":'',
        "active_page":'',
        "show_header":True}

@mod.route('/', methods=["GET"])
def home():
    """
    Renders the view for the home controller.

    :returns: HTML
    :rtype: flask.Response
    """

    args["title"] = "Home"
    args["active_page"] = "Home"
    args["show_header"] = "public"

    # Prevent caching if in debug mode.
    return render_template("public/home.html", args=args)

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

@mod.route('/about', methods=["GET"])
def about():
    """
    Renders the view for the home controller.

    :returns: HTML
    :rtype: flask.Response
    """
    args["title"] = "About"
    args["active_page"] = "about"
    args["stylesheet"] = "about"
    args["show_header"] = "public"

    # Prevent caching if in debug mode.
    return render_template("public/about.html", args=args)
