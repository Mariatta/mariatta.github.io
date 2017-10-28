#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mariatta'
AUTHORS = {
    'Mariatta': 'http://mariatta.ca'
}
SITENAME = 'mariatta.ca'
SITEURL = 'http://mariatta.ca'

PATH = 'content'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/mariatta'),
          ('github', 'https://github.com/Mariatta'),
          ('linkedin', 'https://linkedin.com/in/mariatta'),
          ('paypal', 'https://www.paypal.me/mariatta'),
          ('instagram', 'https://www.instagram.com/mariatta81/'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
DEFAULT_DATE = 'fs'

THEME = 'flex'
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['img', 'extra']

SITETITLE = 'Mariatta'
SITESUBTITLE = ''
SITEDESCRIPTION = ''
SITELOGO = SITEURL + '/img/mariatta.jpeg'
FAVICON = SITEURL + '/img/favicon.ico'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2017

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/CNAME': {'path': ''},
    'extra/keybase.txt': {'path': ''},
}
CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True

# Default theme language.
I18N_TEMPLATES_LANG = 'en'

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

GOOGLE_ANALYTICS = 'UA-89118970-2'