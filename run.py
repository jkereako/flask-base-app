#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Run
    ~~~

    This is the entry point into the application.

    To run the application, open your terminal and type:

    $ python run.py

    :author: Jeff Kereakoglow
    :date: 2014-11-05
    :copyright: (c) 2015 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
from app import app

app.run(host="localhost", port=5000, debug=True)
