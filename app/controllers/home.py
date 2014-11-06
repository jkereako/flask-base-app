#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Home controller
    ~~~~~~~~~~~~~~~
    The home controller.

    :author: Jeff Kereakoglow
    :date: 2014-11-05
    :copyright: (c) 2014 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
from flask import Blueprint, render_template
from app.utils import cache_data, fetch_cached_data

mod = Blueprint("home", __name__)

@mod.route('/', methods=["GET"])
def home():
    """
    Renders the view for the home controller.

    :returns: HTML
    :rtype: flask.Response
    """

    # Check for a cached response
    rv = fetch_cached_data()

    if rv is not None:
        return rv

    out = render_template("home.html")

    # Automatically cached for 15 minutes
    cache_data(out)

    return out
