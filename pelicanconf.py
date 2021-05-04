#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'npz35'
ROBOTS = 'index, follow'

SITENAME = "npz35's blog"
SITETITLE = SITENAME
SITESUBTITLE = SITENAME
SITEDESCRIPTION = SITENAME
# SITELOGO = 'logo.png'
COPYRIGHT_YEAR = datetime.now().year
SITEURL = 'localhost:8000'

THEME = './themes/simplify-theme'
PATH = 'content'

STATIC_PATHS = [
]

SLUGIFY_SOURCE = 'basename'
PAGE_ORDER_BY = 'basename'
PAGES_SORT_ATTRIBUTE = 'source_path'

ARTICLE_PATHS = ['pages']
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
# ARTICLE_PRIMARY_PATH = 'posts'

TIMEZONE = 'Asia/Tokyo'
LOCALE = 'ja_JP'
DEFAULT_LANG = 'ja'

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
