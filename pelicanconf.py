#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Salil Panikkaveettil'
SITENAME = u'AdNabu'
SITEURL = 'https://blog.adnabu.com'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('AdNabu', 'https://adnabu.com/'),)

# Social widget
SOCIAL = (
    ("Facebook", "https://www.facebook.com/adnabu"),
    ("Google+", "https://plus.google.com/+AdnabuOfficial"),
    ("Twitter", "https://twitter.com/adnabu"),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'}
}
DISQUS_SITENAME = "adnabu"
GTM_ID = "GTM-WSW63N"
THEME = "themes/notmyidea"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'related_posts']
RELATED_POSTS_MAX = 5
MENUITEMS = (("AdNabu", "https://www.adnabu.com"),)
