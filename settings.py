# -*- coding: utf-8 -*-

AUTHOR = u'Aquiles Carattino'
SITENAME = u'Python For The Lab'
SITEURL = u'https://www.pythonforthelab.com'
TIMEZONE = 'Europe/Amsterdam'
GITHUB_URL = 'https://github.com/PFTL'
PDF_GENERATOR = False

TEMPLATE_PAGES = {'static_index.html': 'index.html',
                 'search.html': 'search/index.html',
                  'static_books.html': 'books/index.html',}

STATIC_PATHS = ['images', 'static', 'pages']

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'



SITEMAP_SAVE_AS = 'sitemap.xml'
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
        'pages': 'monthly'
    },
    'exclude': ['tag/', 'category/', 'categories.html', 'tags.html', 'search/'],
}


FEED_DOMAIN = 'https://www.pythonforthelab.com'

FEED_RSS = 'feed.rss'

MARKUP = ('rst', 'markdown',)

RELATIVE_URLS = False

INDEX_SAVE_AS = 'blog/index.html'

PLUGIN_PATHS = ['plugins',]
PLUGINS = ['new_pigment', 'header_image', 'tipue_search', 'sitemap']

LOCALE = 'en_US.utf8'

# Where to store the images
HEADERS_FOLDER = 'static/img'
# Force to re-generate the images even if they exist
FORCE_IMG_REBUILD = False
# Default image header for when one is missing
DEFAULT_HEADER = 'static/img/compartments.jpg'

DEFAULT_PAGINATION = 12