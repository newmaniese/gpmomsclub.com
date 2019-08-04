#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Grosse Pointe Mom'
SITENAME = "Grosse Pointe Moms Club"
SITEURL = 'https://www.gpmomsclub.com'

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Activities", "/pages/activities.html"),
#    ("Board", "/pages/moms-club-board.html"),
    ("Calendar", "/pages/calendar.html"),
    ("Membership", "/pages/membership-inquiries.html")
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

STATIC_PATHS = ['images', 'static/robots.txt', 'static/favicon.ico']
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'}
}

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "theme"
