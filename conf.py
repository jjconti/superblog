# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

# !! This is the configuration of Nikola. !! #
# !!  You should edit it to your liking.  !! #


# ! Some settings can be different in different languages.
# ! A comment stating (translatable) is used to denote those.
# ! There are two ways to specify a translatable setting:
# ! (a) BLOG_TITLE = "My Blog"
# ! (b) BLOG_TITLE = {"en": "My Blog", "es": "Mi Blog"}
# ! Option (a) is used when you don't want that setting translated.
# ! Option (b) is used for settings that are different in different languages.


# Data about this site
BLOG_AUTHOR = "Juanjo"  # (translatable)
BLOG_TITLE = "En borrador permanente"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link. Don't forget the protocol (http/https)!
SITE_URL = "http://www.juanjoconti.com/"
# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://www.juanjoconti.com.ar/"
BLOG_EMAIL = "jjconti@gmail.com"
BLOG_DESCRIPTION = "el blog de Juanjo Conti - abstracto, lúdico y digital"  # (translatable)

# Nikola is multilingual!
#
# Currently supported languages are:
#
# en        English
# ar        Arabic
# az        Azerbaijani
# bg        Bulgarian
# bs        Bosnian
# ca        Catalan
# cs        Czech [ALTERNATIVELY cz]
# da        Danish
# de        German
# el        Greek [NOT gr]
# eo        Esperanto
# es        Spanish
# et        Estonian
# eu        Basque
# fa        Persian
# fi        Finnish
# fr        French
# hi        Hindi
# hr        Croatian
# id        Indonesian
# it        Italian
# ja        Japanese [NOT jp]
# ko        Korean
# nb        Norwegian Bokmål
# nl        Dutch
# pa        Punjabi
# pl        Polish
# pt        Portuguese
# pt_br     Portuguese (Brasil)
# ru        Russian
# sk        Slovak
# sl        Slovene
# sr        Serbian (Cyrillic)
# sr_latin  Serbian (Latin)
# sv        Swedish
# tr        Turkish [NOT tr_TR]
# uk        Ukrainian
# ur        Urdu
# zh_cn     Chinese (Simplified)
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (cf. the modules at nikola/data/themes/base/messages/).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "es"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.pl.rst will be considered
# its Polish translation.
#     (in the above example: path == "something", ext == "rst", lang == "pl")
# this pattern is also used for metadata:
#     something.meta -> something.pl.meta

TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"

# Links for the sidebar / navigation bar.  (translatable)
# This is a dict.  The keys are languages, and values are tuples.
#
# For regular links:
#     ('https://getnikola.com/', 'Nikola Homepage')
#
# For submenus:
#     (
#         (
#             ('https://apple.com/', 'Apple'),
#             ('https://orange.com/', 'Orange'),
#         ),
#         'Fruits'
#     )
#
# WARNING: Support for submenus is theme-dependent.
#          Only one level of submenus is supported.
# WARNING: Some themes, including the default Bootstrap 3 theme,
#          may present issues if the menu is too large.
#          (in bootstrap3, the navbar can grow too large and cover contents.)
# WARNING: If you link to directories, make sure to follow
#          ``STRIP_INDEXES``.  If it’s set to ``True``, end your links
#          with a ``/``, otherwise end them with ``/index.html`` — or
#          else they won’t be highlighted when active.

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/que-es-este-blog/", "¿Qué es este blog?"),
        ("/fotos/", "Fotos"),
        ("/archivo/", "Archivo"),
        ("/etiquetas/", "Etiquetas"),
        ("/rss.xml", "RSS"),
    ),
}

# Name of the theme to use.
THEME = "humitos"

# Primary color of your theme. This will be used to customize your theme and
# auto-generate related colors in POSTS_SECTION_COLORS. Must be a HEX value.
THEME_COLOR = '#5670d4'

# Below this point, everything is optional

# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (e.g. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use the ISO 8601/RFC 3339 format (ex. 2012-03-30T23:00:00+02:00)
TIMEZONE = "America/Argentina/Buenos_Aires"

# If you want to use ISO 8601 (also valid RFC 3339) throughout Nikola
# (especially in new_post), set this to True.
# Note that this does not affect DATE_FORMAT.
# FORCE_ISO8601 = False

# Date format used to display post dates.
# (str used by datetime.datetime.strftime)
# DATE_FORMAT = '%Y-%m-%d %H:%M'

# Date format used to display post dates, if local dates are used.
# (str used by moment.js)
# JS_DATE_FORMAT = 'YYYY-MM-DD HH:mm'

# Date fanciness.
#
# 0 = using DATE_FORMAT and TIMEZONE
# 1 = using JS_DATE_FORMAT and local user time (via moment.js)
# 2 = using a string like “2 days ago”
#
# Your theme must support it, bootstrap and bootstrap3 already do.
DATE_FANCINESS = 2

# While Nikola can select a sensible locale for each language,
# sometimes explicit control can come handy.
# In this file we express locales in the string form that
# python's locales will accept in your OS, by example
# "en_US.utf8" in Unix-like OS, "English_United States" in Windows.
# LOCALES = dict mapping language --> explicit locale for the languages
# in TRANSLATIONS. You can omit one or more keys.
# LOCALE_FALLBACK = locale to use when an explicit locale is unavailable
# LOCALE_DEFAULT = locale to use for languages not mentioned in LOCALES; if
# not set the default Nikola mapping is used.

# POSTS and PAGES contains (wildcard, destination, template) tuples.
#
# The wildcard is used to generate a list of reSt source files
# (whatever/thing.txt).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for Spanish, with code "es"):
#     whatever/thing.es.txt and whatever/thing.es.meta
#
#     This assumes you use the default TRANSLATIONS_PATTERN.
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combined with the template to produce rendered
# pages, which will be placed at
# output / TRANSLATIONS[lang] / destination / pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds and are considered part of a blog, while PAGES are
# just independent HTML pages.
#

POSTS = (
    ("posts/nikola/*.rst", "posts", "post.tmpl"),
    ("posts/wordpress/*.md", "posts", "post.tmpl"),
    ("posts/goodreads/*.md", "posts", "post.tmpl"),
    ("posts/twitpic/*.rst", "posts", "post.tmpl"),
    ("posts/nokia/*.rst", "posts", "post.tmpl"),
)

PAGES = (
    ("stories/*.rst", "", "story.tmpl"),
    ("stories/*.txt", "", "story.tmpl"),
    ("stories/wordpress/*.md", "stories", "story.tmpl"),
    ("stories/*.html", "", "story.tmpl"),
)


# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of {source: relative destination}.
# Default is:
FILES_FOLDERS = {'files': ''}
# Which means copy 'files' into 'output'

# One or more folders containing listings to be processed and stored into
# the output. The format is a dictionary of {source: relative destination}.
# Default is:
# LISTINGS_FOLDERS = {'listings': 'listings'}
# Which means process listings from 'listings' into 'output/listings'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# 'rest' is reStructuredText
# 'markdown' is MarkDown
# 'html' assumes the file is HTML and just copies it
COMPILERS = {
    "rest": ('.txt', '.rst'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "html": ('.html', '.htm'),
}

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# If this is set to True, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# If this is set to False, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# Formerly known as HIDE_UNTRANSLATED_POSTS (inverse)
# SHOW_UNTRANSLATED_POSTS = True

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
# LOGO_URL = ''

# If you want to hide the title of your website (for example, if your logo
# already contains the text), set this to False.
# SHOW_BLOG_TITLE = True

# Writes tag cloud data in form of tag_cloud_data.json.
# Warning: this option will change its default value to False in v8!
WRITE_TAG_CLOUD = True

# Generate pages for each section. The site must have at least two sections
# for this option to take effect. It wouldn't build for just one section.
POSTS_SECTIONS = True

# Setting this to False generates a list page instead of an index. Indexes
# are the default and will apply GENERATE_ATOM if set.
# POSTS_SECTIONS_ARE_INDEXES = True

# Each post and section page will have an associated color that can be used
# to style them with a recognizable color detail across your site. A color
# is assigned to  each section based on shifting the hue of your THEME_COLOR
# at least 7.5 % while leaving the lightness and saturation untouched in the
# HUSL colorspace. You can overwrite colors by assigning them colors in HEX.
# POSTS_SECTION_COLORS = {
#     DEFAULT_LANG: {
#         'posts':  '#49b11bf',
#         'reviews':   '#ffe200',
#     },
# }

# Associate a description with a section. For use in meta description on
# section index pages or elsewhere in themes.
# POSTS_SECTION_DESCRIPTIONS = {
#     DEFAULT_LANG: {
#         'how-to': 'Learn how-to things properly with these amazing tutorials.',
#     },
# }

# Sections are determined by their output directory as set in POSTS by default,
# but can alternatively be determined from file metadata instead.
# POSTS_SECTION_FROM_META = False

# Names are determined from the output directory name automatically or the
# metadata label. Unless overwritten below, names will use title cased and
# hyphens replaced by spaces.
# POSTS_SECTION_NAME = {
#    DEFAULT_LANG: {
#        'posts': 'Blog Posts',
#        'uncategorized': 'Odds and Ends',
#    },
# }

# Titles for per-section index pages. Can be either one string where "{name}"
# is substituted or the POSTS_SECTION_NAME, or a dict of sections. Note
# that the INDEX_PAGES option is also applied to section page titles.
# POSTS_SECTION_TITLE = {
#     DEFAULT_LANG: {
#         'how-to': 'How-to and Tutorials',
#     },
# }

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
TAG_PATH = "etiquetas"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
TAG_PAGES_ARE_INDEXES = True

# Set descriptions for tag pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the tag list or index page’s title.
# TAG_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for tag pages. The default is "Posts about TAG".
# TAG_PAGES_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a tag publicly, you can mark it as hidden.
# The tag will not be displayed on the tag list page, the tag cloud and posts.
# Tag pages will still be generated.
HIDDEN_TAGS = ['mathjax']

# Only include tags on the tag list/overview page if there are at least
# TAGLIST_MINIMUM_POSTS number of posts or more with every tag. Every tag
# page is still generated, linked from posts, and included in the sitemap.
# However, more obscure tags can be hidden from the tag index page.
# TAGLIST_MINIMUM_POSTS = 1

# Final locations are:
# output / TRANSLATION[lang] / CATEGORY_PATH / index.html (list of categories)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.html (list of posts for a category)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.xml (RSS feed for a category)
# CATEGORY_PATH = "categories"
# CATEGORY_PREFIX = "cat_"

# If CATEGORY_ALLOW_HIERARCHIES is set to True, categories can be organized in
# hierarchies. For a post, the whole path in the hierarchy must be specified,
# using a forward slash ('/') to separate paths. Use a backslash ('\') to escape
# a forward slash or a backslash (i.e. '\//\\' is a path specifying the
# subcategory called '\' of the top-level category called '/').
CATEGORY_ALLOW_HIERARCHIES = False
# If CATEGORY_OUTPUT_FLAT_HIERARCHY is set to True, the output written to output
# contains only the name of the leaf category and not the whole path.
CATEGORY_OUTPUT_FLAT_HIERARCHY = False

# If CATEGORY_PAGES_ARE_INDEXES is set to True, each category's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# CATEGORY_PAGES_ARE_INDEXES = False

# Set descriptions for category pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the category list or index page’s title.
# CATEGORY_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for category pages. The default is "Posts about CATEGORY".
# CATEGORY_PAGES_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a category publicly, you can mark it as hidden.
# The category will not be displayed on the category list page.
# Category pages will still be generated.
HIDDEN_CATEGORIES = []

# If ENABLE_AUTHOR_PAGES is set to True and there is more than one
# author, author pages are generated.
# ENABLE_AUTHOR_PAGES = True

# Final locations are:
# output / TRANSLATION[lang] / AUTHOR_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / AUTHOR_PATH / author.html (list of posts for a tag)
# output / TRANSLATION[lang] / AUTHOR_PATH / author.xml (RSS feed for a tag)
# AUTHOR_PATH = "authors"

# If AUTHOR_PAGES_ARE_INDEXES is set to True, each author's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# AUTHOR_PAGES_ARE_INDEXES = False

# Set descriptions for author pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the author list or index page’s title.
# AUTHOR_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "Juanjo Conti": "Python coder and writer.",
#        "Roberto Alsina": "Nikola father."
#    },
# }


# If you do not want to display an author publicly, you can mark it as hidden.
# The author will not be displayed on the author list page and posts.
# Tag pages will still be generated.
HIDDEN_AUTHORS = ['Guest']

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# INDEX_PATH = ""

# Create per-month archives instead of per-year
CREATE_MONTHLY_ARCHIVE = True
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Create year, month, and day archives each with a (long) list of posts
# (overrides both CREATE_MONTHLY_ARCHIVE and CREATE_SINGLE_ARCHIVE)
# CREATE_FULL_ARCHIVES = False
# If monthly archives or full archives are created, adds also one archive per day
# CREATE_DAILY_ARCHIVE = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / DAY / index.html
ARCHIVE_PATH = "archivo"
ARCHIVE_FILENAME = "index.html"

# If ARCHIVES_ARE_INDEXES is set to True, each archive page which contains a list
# of posts will contain the posts themselves. If set to False, it will be just a
# list of links.
# ARCHIVES_ARE_INDEXES = False

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# RSS_PATH = ""

# Number of posts in RSS feeds
# FEED_LENGTH = 10

# Slug the Tag URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# Slug the Author URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_AUTHOR_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = [["2013/03/11/fotos-en-el-campo-09032013/index.html", "/posts/2013/03/11/fotos-en-el-campo-09032013.html"], ["libros/santa-furia/index.html", "/stories/libros/santa-furia.html"], ["2014/09/08/cuentos-ilustrados-por-ceruleo/index.html", "/posts/2014/09/08/cuentos-ilustrados-por-ceruleo.html"], ["2010/11/22/dichos-populares-segun-un-programdor/index.html", "/posts/2010/11/22/dichos-populares-segun-un-programdor.html"], ["2012/05/13/asimov-sobre-la-escritura-y-su-reciente-casamiento/index.html", "/posts/2012/05/13/asimov-sobre-la-escritura-y-su-reciente-casamiento.html"], ["2015/04/24/visita-al-dentista-video/index.html", "/posts/2015/04/24/visita-al-dentista-video.html"], ["2014/05/29/bonus-track-para-bolonqui/index.html", "/posts/2014/05/29/bonus-track-para-bolonqui.html"], ["2012/02/19/la-lujuria-para-un-programador/index.html", "/posts/2012/02/19/la-lujuria-para-un-programador.html"], ["2014/05/22/el-dia-que-me-robe-un-chiste-de-quino/index.html", "/posts/2014/05/22/el-dia-que-me-robe-un-chiste-de-quino.html"], ["2015/06/20/audio-de-la-entrevista-en-recreo-diario-sobre-mi-articulo-sobre-el-escrutinio-en-las-elecciones-santa-fe-2015/index.html", "/posts/2015/06/20/audio-de-la-entrevista-en-recreo-diario-sobre-mi-articulo-sobre-el-escrutinio-en-las-elecciones-santa-fe-2015.html"], ["2013/07/12/camaragesell-guillermo-saccomanno/index.html", "/posts/2013/07/12/camaragesell-guillermo-saccomanno.html"], ["2006/03/23/america-latina-en-una-cruzada-por-el-software-libre/index.html", "/posts/2006/03/23/america-latina-en-una-cruzada-por-el-software-libre.html"], ["2009/09/09/software-freedom-day-en-rosario/index.html", "/posts/2009/09/09/software-freedom-day-en-rosario.html"], ["2010/10/02/correccion-ortografica-en-vim/index.html", "/posts/2010/10/02/correccion-ortografica-en-vim.html"], ["2011/12/15/el-hijo-del-escritor/index.html", "/posts/2011/12/15/el-hijo-del-escritor.html"], ["2015/08/11/hoy-tuve-una-suerte-pequena/index.html", "/posts/2015/08/11/hoy-tuve-una-suerte-pequena.html"], ["2010/06/10/paseo-en-barco-estocolmo/index.html", "/posts/2010/06/10/paseo-en-barco-estocolmo.html"], ["2008/12/10/voy-hacia-el-fuego/index.html", "/posts/2008/12/10/voy-hacia-el-fuego.html"], ["2011/10/03/la-maquina-de-los-cuentos-en-revista-libresfera/index.html", "/posts/2011/10/03/la-maquina-de-los-cuentos-en-revista-libresfera.html"], ["2006/08/27/generacion-de-imagenes-con-gd-desde-php/index.html", "/posts/2006/08/27/generacion-de-imagenes-con-gd-desde-php.html"], ["2006/07/22/documental-startupcom/index.html", "/posts/2006/07/22/documental-startupcom.html"], ["2007/11/19/programar/index.html", "/posts/2007/11/19/programar.html"], ["2013/07/14/un-cuento-mio-en-4to-grado/index.html", "/posts/2013/07/14/un-cuento-mio-en-4to-grado.html"], ["2009/07/02/gane-una-de-las-becas-del-programa-bicentenario-de-investigacion-y-posgrado-de-la-utn/index.html", "/posts/2009/07/02/gane-una-de-las-becas-del-programa-bicentenario-de-investigacion-y-posgrado-de-la-utn.html"], ["2006/01/10/gnuplot/index.html", "/posts/2006/01/10/gnuplot.html"], ["2010/01/29/cabanas-cayasta/index.html", "/posts/2010/01/29/cabanas-cayasta.html"], ["2012/05/25/comado-para-las-empanadas/index.html", "/posts/2012/05/25/comado-para-las-empanadas.html"], ["2012/06/09/proyecto-exitoso/index.html", "/posts/2012/06/09/proyecto-exitoso.html"], ["2008/10/04/terminando-pythone-en-santa-fe-2008/index.html", "/posts/2008/10/04/terminando-pythone-en-santa-fe-2008.html"], ["2008/07/27/the-bing-bang-theory-theme-song-bare-naked-ladies/index.html", "/posts/2008/07/27/the-bing-bang-theory-theme-song-bare-naked-ladies.html"], ["2014/12/31/este-ano-cree-automagica/index.html", "/posts/2014/12/31/este-ano-cree-automagica.html"], ["2007/11/27/jargon-fortunes/index.html", "/posts/2007/11/27/jargon-fortunes.html"], ["2012/01/11/policiales/index.html", "/posts/2012/01/11/policiales.html"], ["2008/12/10/el-nino-con-el-pijama-a-rayas/index.html", "/posts/2008/12/10/el-nino-con-el-pijama-a-rayas.html"], ["2014/02/22/lo-que-es-mejor-a-orillas-del-parana-que-en-paris-juan-jose-saer/index.html", "/posts/2014/02/22/lo-que-es-mejor-a-orillas-del-parana-que-en-paris-juan-jose-saer.html"], ["2014/05/09/regalo-algunos-libros-via-goodreads/index.html", "/posts/2014/05/09/regalo-algunos-libros-via-goodreads.html"], ["2015/05/25/video-de-mi-charla-ruby-para-programadores-python/index.html", "/posts/2015/05/25/video-de-mi-charla-ruby-para-programadores-python.html"], ["2014/05/26/multiviral-calle-13/index.html", "/posts/2014/05/26/multiviral-calle-13.html"], ["2012/05/23/olor-a-tinta/index.html", "/posts/2012/05/23/olor-a-tinta.html"], ["2014/10/01/cartones-1-x-dia/index.html", "/posts/2014/10/01/cartones-1-x-dia.html"], ["2008/11/30/primer-experiencia-con-ruby/index.html", "/posts/2008/11/30/primer-experiencia-con-ruby.html"], ["2008/08/22/logica-de-primer-orden/index.html", "/posts/2008/08/22/logica-de-primer-orden.html"], ["2012/12/23/les-regalo-un-libro-por-navidad/index.html", "/posts/2012/12/23/les-regalo-un-libro-por-navidad.html"], ["2006/03/12/comparacion-entre-las-ediciones-3ra-y-4ta-del-libro-redes-de-computadoras-de-andrew-s-tanenbaum/index.html", "/posts/2006/03/12/comparacion-entre-las-ediciones-3ra-y-4ta-del-libro-redes-de-computadoras-de-andrew-s-tanenbaum.html"], ["2010/07/11/como-cambiar-el-puerto-de-salida-por-defecto-de-ssh/index.html", "/posts/2010/07/11/como-cambiar-el-puerto-de-salida-por-defecto-de-ssh.html"], ["2009/05/03/budin-de-pera/index.html", "/posts/2009/05/03/budin-de-pera.html"], ["2006/01/13/encontre-mi-carpeta-de-algoritmos-d/index.html", "/posts/2006/01/13/encontre-mi-carpeta-de-algoritmos-d.html"], ["2010/12/19/lines-of-code/index.html", "/posts/2010/12/19/lines-of-code.html"], ["2006/04/22/cada-cosa-en-su-lugar/index.html", "/posts/2006/04/22/cada-cosa-en-su-lugar.html"], ["2012/05/24/vision-robotica/index.html", "/posts/2012/05/24/vision-robotica.html"], ["2012/10/27/charla-entre-escritores-humor/index.html", "/posts/2012/10/27/charla-entre-escritores-humor.html"], ["2012/04/11/a-las-pinas-con-la-ortografia/index.html", "/posts/2012/04/11/a-las-pinas-con-la-ortografia.html"], ["2011/12/30/saludo-de-ano-nuevo-2012/index.html", "/posts/2011/12/30/saludo-de-ano-nuevo-2012.html"], ["2010/09/26/twitter-updates-desde-twisted/index.html", "/posts/2010/09/26/twitter-updates-desde-twisted.html"], ["2010/07/24/diccionario-bidireccional-en-python/index.html", "/posts/2010/07/24/diccionario-bidireccional-en-python.html"], ["2006/02/04/los-justos-una-de-tantas-historias-detras-del-p2p/index.html", "/posts/2006/02/04/los-justos-una-de-tantas-historias-detras-del-p2p.html"], ["2012/05/15/choripanes/index.html", "/posts/2012/05/15/choripanes.html"], ["2010/07/06/talk-taint-mode-for-python-via-a-library-slides/index.html", "/posts/2010/07/06/talk-taint-mode-for-python-via-a-library-slides.html"], ["2008/06/27/generar-archivos-rtf-en-forma-dinamica-desde-django/index.html", "/posts/2008/06/27/generar-archivos-rtf-en-forma-dinamica-desde-django.html"], ["2006/02/08/dia-aeropuerto/index.html", "/posts/2006/02/08/dia-aeropuerto.html"], ["2014/12/31/cuento-bicicleta-video/index.html", "/posts/2014/12/31/cuento-bicicleta-video.html"], ["2007/12/29/manipulacion-de-pixels-con-python-fu/index.html", "/posts/2007/12/29/manipulacion-de-pixels-con-python-fu.html"], ["2010/09/08/fotografiando-desde-el-camino-segunda-edicion/index.html", "/posts/2010/09/08/fotografiando-desde-el-camino-segunda-edicion.html"], ["2014/01/07/este-ano-voy-a-intentar-usar-goodreads/index.html", "/posts/2014/01/07/este-ano-voy-a-intentar-usar-goodreads.html"], ["2010/02/25/los-6-magnificos-divertimentos-matematicos/index.html", "/posts/2010/02/25/los-6-magnificos-divertimentos-matematicos.html"], ["2010/08/30/fotos-en-el-campo/index.html", "/posts/2010/08/30/fotos-en-el-campo.html"], ["2010/05/09/charla-entendiendo-decoradores-en-python/index.html", "/posts/2010/05/09/charla-entendiendo-decoradores-en-python.html"], ["2009/04/04/la-historia-de-python-el-uso-de-tipado-dinamico/index.html", "/posts/2009/04/04/la-historia-de-python-el-uso-de-tipado-dinamico.html"], ["2012/02/09/sonetos/index.html", "/posts/2012/02/09/sonetos.html"], ["2008/10/01/cosas-y-humanos/index.html", "/posts/2008/10/01/cosas-y-humanos.html"], ["2010/08/20/el-hosting-para-django-mas-barato/index.html", "/posts/2010/08/20/el-hosting-para-django-mas-barato.html"], ["2007/04/19/shuffle-un-diccionario-en-python/index.html", "/posts/2007/04/19/shuffle-un-diccionario-en-python.html"], ["2007/10/01/3-razones-fundamentales-por-las-cuales-el-estado-debe-usar-software-libre/index.html", "/posts/2007/10/01/3-razones-fundamentales-por-las-cuales-el-estado-debe-usar-software-libre.html"], ["2006/11/07/el-paquete-de-galletitas/index.html", "/posts/2006/11/07/el-paquete-de-galletitas.html"], ["2009/03/26/el-segundo-color-predominante-pil/index.html", "/posts/2009/03/26/el-segundo-color-predominante-pil.html"], ["2012/02/06/llego-la-orsai-5-a-santa-fe/index.html", "/posts/2012/02/06/llego-la-orsai-5-a-santa-fe.html"], ["2006/11/16/pueblos-originarios-y-software-libre/index.html", "/posts/2006/11/16/pueblos-originarios-y-software-libre.html"], ["2010/11/10/si-te-gusta-leer-y-vivis-en-santa-fe-tenes-que-ser-socio-de-la-biblioteca-pedagogica/index.html", "/posts/2010/11/10/si-te-gusta-leer-y-vivis-en-santa-fe-tenes-que-ser-socio-de-la-biblioteca-pedagogica.html"], ["2011/03/15/python-guardar-imagenes-en-una-base-de-datos-sqlite/index.html", "/posts/2011/03/15/python-guardar-imagenes-en-una-base-de-datos-sqlite.html"], ["2009/03/09/cocarroy/index.html", "/posts/2009/03/09/cocarroy.html"], ["2007/07/28/wp-en-espanol/index.html", "/posts/2007/07/28/wp-en-espanol.html"], ["2015/01/01/los-libros-que-me-regalaron-para-el-cumpleanos-y-navidad/index.html", "/posts/2015/01/01/los-libros-que-me-regalaron-para-el-cumpleanos-y-navidad.html"], ["2007/12/18/las-3-partes-del-criptonomicon/index.html", "/posts/2007/12/18/las-3-partes-del-criptonomicon.html"], ["2009/03/11/la-historia-de-python-microsoft-distribuye-codigo-python-en-1996/index.html", "/posts/2009/03/11/la-historia-de-python-microsoft-distribuye-codigo-python-en-1996.html"], ["2010/03/03/os-path-en-el-settings-py-de-django-para-mayor-comodidad/index.html", "/posts/2010/03/03/os-path-en-el-settings-py-de-django-para-mayor-comodidad.html"], ["2009/03/05/tuya-de-claudia-pineiro/index.html", "/posts/2009/03/05/tuya-de-claudia-pineiro.html"], ["2012/09/22/nico-cesar-se-va-a-vivir-a-boston/index.html", "/posts/2012/09/22/nico-cesar-se-va-a-vivir-a-boston.html"], ["2013/11/08/cuento-en-yerba-fanzine-5/index.html", "/posts/2013/11/08/cuento-en-yerba-fanzine-5.html"], ["2011/03/20/documental-el-pueblo-de-los-pianos/index.html", "/posts/2011/03/20/documental-el-pueblo-de-los-pianos.html"], ["2007/12/05/python-en-xkcd/index.html", "/posts/2007/12/05/python-en-xkcd.html"], ["2014/09/11/el-sabado-al-as-18-hs-en-la-feria-del-libro-de-santa-fe/index.html", "/posts/2014/09/11/el-sabado-al-as-18-hs-en-la-feria-del-libro-de-santa-fe.html"], ["2008/08/08/hay-un-nuevo-ingeniero-en-la-ciudad/index.html", "/posts/2008/08/08/hay-un-nuevo-ingeniero-en-la-ciudad.html"], ["2007/07/07/260/index.html", "/posts/2007/07/07/260.html"], ["2013/07/12/algunas-fotos-de-las-vacaciones-en-mexico/index.html", "/posts/2013/07/12/algunas-fotos-de-las-vacaciones-en-mexico.html"], ["2010/10/12/historias-en-internet-el-busto-de-carlos-pellegrini/index.html", "/posts/2010/10/12/historias-en-internet-el-busto-de-carlos-pellegrini.html"], ["2006/01/08/tartagliapy/index.html", "/posts/2006/01/08/tartagliapy.html"], ["2007/12/23/algunas-fotos-de-mi-cumple-n%c2%b0-23/index.html", "/posts/2007/12/23/algunas-fotos-de-mi-cumple-nadeg-23.html"], ["2009/06/25/la-historia-de-python-como-las-excepciones-llegaron-a-ser-clases/index.html", "/posts/2009/06/25/la-historia-de-python-como-las-excepciones-llegaron-a-ser-clases.html"], ["2005/09/08/%c2%bfes-el-software-un-arte/index.html", "/posts/2005/09/08/aes-el-software-un-arte.html"], ["2008/09/23/4-de-octubre-3ra-jornada-python-en-santa-fe/index.html", "/posts/2008/09/23/4-de-octubre-3ra-jornada-python-en-santa-fe.html"], ["2011/02/24/para-entender-el-origen-de-narnia/index.html", "/posts/2011/02/24/para-entender-el-origen-de-narnia.html"], ["2006/06/13/nueva-direccion-de-email/index.html", "/posts/2006/06/13/nueva-direccion-de-email.html"], ["2008/10/30/alimentando-un-intrepid-ibex/index.html", "/posts/2008/10/30/alimentando-un-intrepid-ibex.html"], ["libros/cuentos4/index.html", "/stories/libros/cuentos4.html"], ["2011/09/20/honor-ilustrado/index.html", "/posts/2011/09/20/honor-ilustrado.html"], ["2011/01/30/la-sole-pastorutti-twittea-sobre-kiko-opertti/index.html", "/posts/2011/01/30/la-sole-pastorutti-twittea-sobre-kiko-opertti.html"], ["2010/07/16/asimov-sobre-inteligencia-artificial/index.html", "/posts/2010/07/16/asimov-sobre-inteligencia-artificial.html"], ["2008/11/03/tiempo-de-valientes/index.html", "/posts/2008/11/03/tiempo-de-valientes.html"], ["2009/04/20/tortitas-negras/index.html", "/posts/2009/04/20/tortitas-negras.html"], ["2007/10/22/pata-vos-freud/index.html", "/posts/2007/10/22/pata-vos-freud.html"], ["2009/04/08/pan-de-salvado/index.html", "/posts/2009/04/08/pan-de-salvado.html"], ["2009/04/12/rosca-de-pascua/index.html", "/posts/2009/04/12/rosca-de-pascua.html"], ["2011/02/07/tip-para-leer-la-biblioteca-de-los-muertos/index.html", "/posts/2011/02/07/tip-para-leer-la-biblioteca-de-los-muertos.html"], ["2013/04/04/mar-chiquita/index.html", "/posts/2013/04/04/mar-chiquita.html"], ["2007/09/13/twisted-zombie-para-windows/index.html", "/posts/2007/09/13/twisted-zombie-para-windows.html"], ["2009/12/30/decoradores-en-python-iii/index.html", "/posts/2009/12/30/decoradores-en-python-iii.html"], ["2008/06/28/django-messages-en-espanol/index.html", "/posts/2008/06/28/django-messages-en-espanol.html"], ["2007/07/25/mais-desaparecidos-en-thunderbird/index.html", "/posts/2007/07/25/mais-desaparecidos-en-thunderbird.html"], ["2012/05/20/el-otro-espejo-cuento/index.html", "/posts/2012/05/20/el-otro-espejo-cuento.html"], ["2006/01/08/una-pizca-de-programacion-funcional-en-python/index.html", "/posts/2006/01/08/una-pizca-de-programacion-funcional-en-python.html"], ["2012/08/23/la-convencion/index.html", "/posts/2012/08/23/la-convencion.html"], ["2012/07/30/los-caballeros-de-la-rosa-impreso/index.html", "/posts/2012/07/30/los-caballeros-de-la-rosa-impreso.html"], ["2014/09/11/charlas-con-el-hemisferio-derecho-de-hernan-casciari/index.html", "/posts/2014/09/11/charlas-con-el-hemisferio-derecho-de-hernan-casciari.html"], ["2014/10/08/conocer-a-oyola/index.html", "/posts/2014/10/08/conocer-a-oyola.html"], ["2008/10/10/controles-de-acceso-biometricos/index.html", "/posts/2008/10/10/controles-de-acceso-biometricos.html"], ["2006/09/11/programacion-temporal-de-eventos-con-python/index.html", "/posts/2006/09/11/programacion-temporal-de-eventos-con-python.html"], ["2014/09/23/paso-la-feria-del-libro/index.html", "/posts/2014/09/23/paso-la-feria-del-libro.html"], ["2010/06/13/postales-de-gotemburgo/index.html", "/posts/2010/06/13/postales-de-gotemburgo.html"], ["2010/05/10/borrar-todos-los-archivos-de-un-directorio-menos-los-que/index.html", "/posts/2010/05/10/borrar-todos-los-archivos-de-un-directorio-menos-los-que.html"], ["2014/10/08/seguimos-con-los-cartones/index.html", "/posts/2014/10/08/seguimos-con-los-cartones.html"], ["2007/03/21/lecturas-de-verano/index.html", "/posts/2007/03/21/lecturas-de-verano.html"], ["libros/la-prueba/index.html", "/stories/libros/la-prueba.html"], ["2007/07/10/beatriz-busaniche-habla-sobre-desigualdades-sociales-en-santa-fe/index.html", "/posts/2007/07/10/beatriz-busaniche-habla-sobre-desigualdades-sociales-en-santa-fe.html"], ["2010/10/08/%c2%bftelevolucion/index.html", "/posts/2010/10/08/atelevolucion.html"], ["2012/06/03/en-la-11-feria-del-libro-de-carlos-pellegrini/index.html", "/posts/2012/06/03/en-la-11-feria-del-libro-de-carlos-pellegrini.html"], ["2011/10/28/jornada-de-cultura-libre-en-santa-fe/index.html", "/posts/2011/10/28/jornada-de-cultura-libre-en-santa-fe.html"], ["2009/12/29/como-agregar-meneame-a-bookmarkify/index.html", "/posts/2009/12/29/como-agregar-meneame-a-bookmarkify.html"], ["2005/10/03/if-you-dont-you-should-3-lecturas-recomendadas/index.html", "/posts/2005/10/03/if-you-dont-you-should-3-lecturas-recomendadas.html"], ["2011/05/22/el-padrino/index.html", "/posts/2011/05/22/el-padrino.html"], ["2006/09/22/el-abandonador-de-libros/index.html", "/posts/2006/09/22/el-abandonador-de-libros.html"], ["2006/09/26/beta-11-de-radiofrecuencia/index.html", "/posts/2006/09/26/beta-11-de-radiofrecuencia.html"], ["2009/09/06/charla-relampago-comet-en-twisted/index.html", "/posts/2009/09/06/charla-relampago-comet-en-twisted.html"], ["2007/02/24/el-estilo-hp/index.html", "/posts/2007/02/24/el-estilo-hp.html"], ["2012/04/04/me-case/index.html", "/posts/2012/04/04/me-case.html"], ["2012/01/15/fiesta-nacional-de-las-culturas/index.html", "/posts/2012/01/15/fiesta-nacional-de-las-culturas.html"], ["2010/01/21/alarmas-en-gnome/index.html", "/posts/2010/01/21/alarmas-en-gnome.html"], ["2009/10/17/cuadro-de-honor/index.html", "/posts/2009/10/17/cuadro-de-honor.html"], ["software/index.html", "/stories/software.html"], ["2006/10/20/5tas-conferencias-abiertas-de-gnulinux-y-software-libre-cafeconf/index.html", "/posts/2006/10/20/5tas-conferencias-abiertas-de-gnulinux-y-software-libre-cafeconf.html"], ["2014/10/20/feria-del-libro-de-santo-tome/index.html", "/posts/2014/10/20/feria-del-libro-de-santo-tome.html"], ["2008/04/19/que-aprendi-este-pyweek/index.html", "/posts/2008/04/19/que-aprendi-este-pyweek.html"], ["2013/12/31/una-foto-por-cada-mes-del-2013/index.html", "/posts/2013/12/31/una-foto-por-cada-mes-del-2013.html"], ["2012/02/01/backup-de-recuerdos/index.html", "/posts/2012/02/01/backup-de-recuerdos.html"], ["2007/11/08/derrumbando-la-fortaleza-digital/index.html", "/posts/2007/11/08/derrumbando-la-fortaleza-digital.html"], ["2006/03/31/quiero-obtener-el-minimo-cuadrado-perfecto-mayor-a-n/index.html", "/posts/2006/03/31/quiero-obtener-el-minimo-cuadrado-perfecto-mayor-a-n.html"], ["2010/10/12/el-hack-del-dia-como-usar-citrix-desde-ubuntu/index.html", "/posts/2010/10/12/el-hack-del-dia-como-usar-citrix-desde-ubuntu.html"], ["2012/01/20/julio-cortazar-a-fondo/index.html", "/posts/2012/01/20/julio-cortazar-a-fondo.html"], ["2012/04/25/entrevista-a-casciari-lo-que-se-viene-en-orsai/index.html", "/posts/2012/04/25/entrevista-a-casciari-lo-que-se-viene-en-orsai.html"], ["2007/06/24/este-es-un-sitio-verde/index.html", "/posts/2007/06/24/este-es-un-sitio-verde.html"], ["2011/09/11/enrique-alejandro-cantarutti-arte-con-chatarra/index.html", "/posts/2011/09/11/enrique-alejandro-cantarutti-arte-con-chatarra.html"], ["2010/06/20/en-el-archipielago-de-gotemburgo/index.html", "/posts/2010/06/20/en-el-archipielago-de-gotemburgo.html"], ["2012/04/12/ya-podes-comprar-mi-nuevo-libro-de-cuentos/index.html", "/posts/2012/04/12/ya-podes-comprar-mi-nuevo-libro-de-cuentos.html"], ["2010/08/08/argparse-command-line-option-and-argument-parsing/index.html", "/posts/2010/08/08/argparse-command-line-option-and-argument-parsing.html"], ["2007/01/31/python-multiplataforma-ospathjoin/index.html", "/posts/2007/01/31/python-multiplataforma-ospathjoin.html"], ["2009/06/26/fito-en-el-municipal/index.html", "/posts/2009/06/26/fito-en-el-municipal.html"], ["2011/03/15/fotos-de-la-reserva-ecologica-de-la-unl/index.html", "/posts/2011/03/15/fotos-de-la-reserva-ecologica-de-la-unl.html"], ["2006/11/10/saliendo-para-capital-federal/index.html", "/posts/2006/11/10/saliendo-para-capital-federal.html"], ["2012/04/26/ya-junte-la-mitad-de-lo-que-necesito-para-imprimir-mi-libro/index.html", "/posts/2012/04/26/ya-junte-la-mitad-de-lo-que-necesito-para-imprimir-mi-libro.html"], ["2007/03/15/boletin-de-anuncios-de-fundacion-via-libre/index.html", "/posts/2007/03/15/boletin-de-anuncios-de-fundacion-via-libre.html"], ["2014/09/18/videos-en-la-feria-del-libro-de-santa-fe-2014-martes/index.html", "/posts/2014/09/18/videos-en-la-feria-del-libro-de-santa-fe-2014-martes.html"], ["2007/03/30/chestallman/index.html", "/posts/2007/03/30/chestallman.html"], ["2012/01/21/vos-pone-cara-de-borges-que-yo-pongo-cara-de-cortazar/index.html", "/posts/2012/01/21/vos-pone-cara-de-borges-que-yo-pongo-cara-de-cortazar.html"], ["2014/09/19/lo-primero-que-lei-de-selva-almada/index.html", "/posts/2014/09/19/lo-primero-que-lei-de-selva-almada.html"], ["2009/04/09/shell-python-administrativo-sobre-ssh-para-tu-servidor-twisted-en-10-lineas/index.html", "/posts/2009/04/09/shell-python-administrativo-sobre-ssh-para-tu-servidor-twisted-en-10-lineas.html"], ["2007/04/21/n-puzzle/index.html", "/posts/2007/04/21/n-puzzle.html"], ["2010/02/06/aplicar-un-decorador-a-todas-las-funciones-de-un-modulo-en-python/index.html", "/posts/2010/02/06/aplicar-un-decorador-a-todas-las-funciones-de-un-modulo-en-python.html"], ["2008/09/20/aima-en-python/index.html", "/posts/2008/09/20/aima-en-python.html"], ["2007/11/02/minilisp-un-ejemplo-de-ply/index.html", "/posts/2007/11/02/minilisp-un-ejemplo-de-ply.html"], ["2005/09/04/el-derecho-a-leer/index.html", "/posts/2005/09/04/el-derecho-a-leer.html"], ["2009/01/01/citas-sobre-programacion/index.html", "/posts/2009/01/01/citas-sobre-programacion.html"], ["2009/03/25/una-clase-para-usuarios-no-informaticos-de-wordpress/index.html", "/posts/2009/03/25/una-clase-para-usuarios-no-informaticos-de-wordpress.html"], ["2010/04/10/la-historia-de-python-los-origenes-de-las-caracteristicas-funcionales-de-python/index.html", "/posts/2010/04/10/la-historia-de-python-los-origenes-de-las-caracteristicas-funcionales-de-python.html"], ["2010/10/27/algunos-problemas-y-soluciones-al-levantar-bases-de-datos-legacy-con-django/index.html", "/posts/2010/10/27/algunos-problemas-y-soluciones-al-levantar-bases-de-datos-legacy-con-django.html"], ["2007/05/11/flisol-en-tn-ciencias/index.html", "/posts/2007/05/11/flisol-en-tn-ciencias.html"], ["2012/12/15/tesis-de-maestria/index.html", "/posts/2012/12/15/tesis-de-maestria.html"], ["2009/11/27/prolog-un-lenguaje-realmente-diferente/index.html", "/posts/2009/11/27/prolog-un-lenguaje-realmente-diferente.html"], ["2007/09/30/robos-cerca-de-la-facultad/index.html", "/posts/2007/09/30/robos-cerca-de-la-facultad.html"], ["2011/07/31/el-nuevo-paraiso-de-los-tontos/index.html", "/posts/2011/07/31/el-nuevo-paraiso-de-los-tontos.html"], ["2012/05/01/regalo-3-libros-gastos-de-envio-incluidos/index.html", "/posts/2012/05/01/regalo-3-libros-gastos-de-envio-incluidos.html"], ["2010/07/08/fotos-publicadas-por-owasp-app-sec-research-2010/index.html", "/posts/2010/07/08/fotos-publicadas-por-owasp-app-sec-research-2010.html"], ["2008/12/17/casi-ingenieros/index.html", "/posts/2008/12/17/casi-ingenieros.html"], ["2007/05/01/flisol-2007-en-santa-fe/index.html", "/posts/2007/05/01/flisol-2007-en-santa-fe.html"], ["2009/04/26/cookies-de-avena-y-pasas/index.html", "/posts/2009/04/26/cookies-de-avena-y-pasas.html"], ["2013/07/20/el-brochet-como-metafora-de-la-amistad/index.html", "/posts/2013/07/20/el-brochet-como-metafora-de-la-amistad.html"], ["2009/05/04/urls-elegantes-con-django/index.html", "/posts/2009/05/04/urls-elegantes-con-django.html"], ["2009/12/01/entorno-de-desarrollo-swi-prolog/index.html", "/posts/2009/12/01/entorno-de-desarrollo-swi-prolog.html"], ["2009/11/02/conjuntos-en-python/index.html", "/posts/2009/11/02/conjuntos-en-python.html"], ["2011/01/22/narnia/index.html", "/posts/2011/01/22/narnia.html"], ["2015/06/20/tarta-de-frutilla/index.html", "/posts/2015/06/20/tarta-de-frutilla.html"], ["2009/04/25/la-historia-de-python-todo-de-primera-clase/index.html", "/posts/2009/04/25/la-historia-de-python-todo-de-primera-clase.html"], ["2012/06/05/kryptonita/index.html", "/posts/2012/06/05/kryptonita.html"], ["2009/12/08/cuando-todo-lo-demas-falle/index.html", "/posts/2009/12/08/cuando-todo-lo-demas-falle.html"], ["2008/10/20/747/index.html", "/posts/2008/10/20/747.html"], ["2009/01/31/me-on-twitter/index.html", "/posts/2009/01/31/me-on-twitter.html"], ["2007/12/01/rompecabezas-t-enunciado/index.html", "/posts/2007/12/01/rompecabezas-t-enunciado.html"], ["2008/11/02/una-peli-smart-people/index.html", "/posts/2008/11/02/una-peli-smart-people.html"], ["2007/11/24/el-monstruo-subatomico/index.html", "/posts/2007/11/24/el-monstruo-subatomico.html"], ["2007/04/27/probando-scribefire/index.html", "/posts/2007/04/27/probando-scribefire.html"], ["2010/08/16/borges-hacker/index.html", "/posts/2010/08/16/borges-hacker.html"], ["2013/11/18/preventa-xolopes/index.html", "/posts/2013/11/18/preventa-xolopes.html"], ["2007/06/11/fin-de-semana-pythonico/index.html", "/posts/2007/06/11/fin-de-semana-pythonico.html"], ["2006/06/22/spam-nuestro-de-cada-dia/index.html", "/posts/2006/06/22/spam-nuestro-de-cada-dia.html"], ["2008/11/24/el-mejor-hosting-para-django/index.html", "/posts/2008/11/24/el-mejor-hosting-para-django.html"], ["2010/11/02/quoted/index.html", "/posts/2010/11/02/quoted.html"], ["2008/10/15/a-vs-avara/index.html", "/posts/2008/10/15/a-vs-avara.html"], ["2005/11/04/de-regreso-en-la-internet/index.html", "/posts/2005/11/04/de-regreso-en-la-internet.html"], ["2010/10/05/nadie-leyo-biografia-de-un-superheroe/index.html", "/posts/2010/10/05/nadie-leyo-biografia-de-un-superheroe.html"], ["2014/12/17/las-ultimas-cuatro-novelas-que-lei/index.html", "/posts/2014/12/17/las-ultimas-cuatro-novelas-que-lei.html"], ["2008/12/13/licencias-libres-y-libertinas/index.html", "/posts/2008/12/13/licencias-libres-y-libertinas.html"], ["2007/03/11/carta-abierta-a-steve-jobs-para-detener-los-drm/index.html", "/posts/2007/03/11/carta-abierta-a-steve-jobs-para-detener-los-drm.html"], ["2006/06/14/ponete-las-pilas/index.html", "/posts/2006/06/14/ponete-las-pilas.html"], ["2008/08/24/jornadas-regionales-de-software-libre-en-pagian-12/index.html", "/posts/2008/08/24/jornadas-regionales-de-software-libre-en-pagian-12.html"], ["2009/05/28/euler-1-python/index.html", "/posts/2009/05/28/euler-1-python.html"], ["2013/01/28/recorriendo-los-murales-de-carlos-pellegrini/index.html", "/posts/2013/01/28/recorriendo-los-murales-de-carlos-pellegrini.html"], ["2011/04/03/sobre-ver-peliculas-antes-de-leer-las-novelas/index.html", "/posts/2011/04/03/sobre-ver-peliculas-antes-de-leer-las-novelas.html"], ["2008/10/07/un-ejemplo-de-busqueda-a/index.html", "/posts/2008/10/07/un-ejemplo-de-busqueda-a.html"], ["2008/04/15/djangodash/index.html", "/posts/2008/04/15/djangodash.html"], ["2010/08/13/salio-la-revista-de-pyar/index.html", "/posts/2010/08/13/salio-la-revista-de-pyar.html"], ["2012/06/19/el-hombre-que-sono-con-su-gato/index.html", "/posts/2012/06/19/el-hombre-que-sono-con-su-gato.html"], ["2009/08/24/donde-no-hay-seguridad-nadie-puede-romperla/index.html", "/posts/2009/08/24/donde-no-hay-seguridad-nadie-puede-romperla.html"], ["2009/10/21/charla-bienvenido-a-python-en-instituto-libre-09/index.html", "/posts/2009/10/21/charla-bienvenido-a-python-en-instituto-libre-09.html"], ["2011/04/04/mi-libro-de-cuentos-a-la-feria-del-libro/index.html", "/posts/2011/04/04/mi-libro-de-cuentos-a-la-feria-del-libro.html"], ["2013/05/18/cuentos-sobre-subtes/index.html", "/posts/2013/05/18/cuentos-sobre-subtes.html"], ["2007/06/15/mi-primer-clase-en-la-universidad/index.html", "/posts/2007/06/15/mi-primer-clase-en-la-universidad.html"], ["2011/07/30/el-tortoni-en-cepia/index.html", "/posts/2011/07/30/el-tortoni-en-cepia.html"], ["2007/12/03/rompecabezas-t-solucion/index.html", "/posts/2007/12/03/rompecabezas-t-solucion.html"], ["libros/index.html", "/stories/libros.html"], ["2010/04/03/servidor-smtp-para-hacer-pruebas/index.html", "/posts/2010/04/03/servidor-smtp-para-hacer-pruebas.html"], ["2006/02/28/carlos-pellegrini-en-wikipedia/index.html", "/posts/2006/02/28/carlos-pellegrini-en-wikipedia.html"], ["2005/09/06/el-que-tendria-que-haber-sido-mi-primer-post/index.html", "/posts/2005/09/06/el-que-tendria-que-haber-sido-mi-primer-post.html"], ["2012/01/16/oficialmente-distribuidor-amateur-de-orsai/index.html", "/posts/2012/01/16/oficialmente-distribuidor-amateur-de-orsai.html"], ["2009/06/07/dia-del-ingeniero/index.html", "/posts/2009/06/07/dia-del-ingeniero.html"], ["2008/10/19/torta-de-banana-y-chocolate/index.html", "/posts/2008/10/19/torta-de-banana-y-chocolate.html"], ["2006/05/30/fermat-vs-pythagoras-mejorado/index.html", "/posts/2006/05/30/fermat-vs-pythagoras-mejorado.html"], ["2009/01/20/asociacion-de-metodos-en-tiempo-de-ejecucion-en-python/index.html", "/posts/2009/01/20/asociacion-de-metodos-en-tiempo-de-ejecucion-en-python.html"], ["2010/11/06/charla-desarrollando-aplicaciones-de-red-con-twisted/index.html", "/posts/2010/11/06/charla-desarrollando-aplicaciones-de-red-con-twisted.html"], ["2012/12/09/siete-el-tigre-harapiento/index.html", "/posts/2012/12/09/siete-el-tigre-harapiento.html"], ["2009/03/18/la-historia-de-python-el-principio-del-diseno-y-desarrollo-del-lenguaje/index.html", "/posts/2009/03/18/la-historia-de-python-el-principio-del-diseno-y-desarrollo-del-lenguaje.html"], ["2010/08/06/puedo-disfrazar-cualquier-cosa-de-modbus/index.html", "/posts/2010/08/06/puedo-disfrazar-cualquier-cosa-de-modbus.html"], ["2010/08/21/en-borrador-permanente/index.html", "/posts/2010/08/21/en-borrador-permanente.html"], ["2008/10/24/listas-por-comprension-en-python/index.html", "/posts/2008/10/24/listas-por-comprension-en-python.html"], ["2014/02/02/termine-de-leer-doctor-sueno/index.html", "/posts/2014/02/02/termine-de-leer-doctor-sueno.html"], ["2007/01/29/el-yotivenco/index.html", "/posts/2007/01/29/el-yotivenco.html"], ["2007/11/22/really-free-images/index.html", "/posts/2007/11/22/really-free-images.html"], ["2005/12/29/aprendiendo-python/index.html", "/posts/2005/12/29/aprendiendo-python.html"], ["2010/05/24/es-dificil-escribir-las-reglas-de-un-juego/index.html", "/posts/2010/05/24/es-dificil-escribir-las-reglas-de-un-juego.html"], ["2013/04/26/la-caja-cuento/index.html", "/posts/2013/04/26/la-caja-cuento.html"], ["2011/01/25/leyendo-sobre-javascript/index.html", "/posts/2011/01/25/leyendo-sobre-javascript.html"], ["2006/11/29/cargar-programas-graficos-como-un-usuario-distinto-al-que-que-se-ha-logueado/index.html", "/posts/2006/11/29/cargar-programas-graficos-como-un-usuario-distinto-al-que-que-se-ha-logueado.html"], ["2006/04/24/diagramas-de-constelaciones-qam-y-psk/index.html", "/posts/2006/04/24/diagramas-de-constelaciones-qam-y-psk.html"], ["2009/03/16/me-recomendas-un-libro-para-leer/index.html", "/posts/2009/03/16/me-recomendas-un-libro-para-leer.html"], ["2012/01/25/cambiar-foto-de-perfil-en-twitter-cuando-la-cambio-en-facebook/index.html", "/posts/2012/01/25/cambiar-foto-de-perfil-en-twitter-cuando-la-cambio-en-facebook.html"], ["2008/09/28/acomodar-imagenes-con-gqview/index.html", "/posts/2008/09/28/acomodar-imagenes-con-gqview.html"], ["2007/09/20/una-historia-de-emoticons/index.html", "/posts/2007/09/20/una-historia-de-emoticons.html"], ["articulos/index.html", "/stories/articulos.html"], ["2009/08/15/django-middleware/index.html", "/posts/2009/08/15/django-middleware.html"], ["2011/09/18/luis-pescetti-en-la-feria-del-libro-de-santa-fe-2011/index.html", "/posts/2011/09/18/luis-pescetti-en-la-feria-del-libro-de-santa-fe-2011.html"], ["2012/08/11/el-prisionero-del-cielo/index.html", "/posts/2012/08/11/el-prisionero-del-cielo.html"], ["2009/03/24/zinnia/index.html", "/posts/2009/03/24/zinnia.html"], ["2007/10/09/viendo-a-los-conectores-logicos-como-relaciones-entre-conjuntos/index.html", "/posts/2007/10/09/viendo-a-los-conectores-logicos-como-relaciones-entre-conjuntos.html"], ["2011/01/05/i-see-you/index.html", "/posts/2011/01/05/i-see-you.html"], ["2012/01/15/%c2%bfcon-que-libro-seguir/index.html", "/posts/2012/01/15/acon-que-libro-seguir.html"], ["2005/11/04/breve-historia-de-la-cultura-hacker/index.html", "/posts/2005/11/04/breve-historia-de-la-cultura-hacker.html"], ["2008/11/22/33%c2%b0-colacion-y-fiesta-de-fin-de-ano-en-la-facultad/index.html", "/posts/2008/11/22/33adeg-colacion-y-fiesta-de-fin-de-ano-en-la-facultad.html"], ["2007/09/22/nos-subimos-al-podio-de-pyweek-5/index.html", "/posts/2007/09/22/nos-subimos-al-podio-de-pyweek-5.html"], ["2012/02/02/charlas-en-el-subte/index.html", "/posts/2012/02/02/charlas-en-el-subte.html"], ["2008/08/25/notas-para-tener-en-cuenta-a-la-hora-de-instalar-savi/index.html", "/posts/2008/08/25/notas-para-tener-en-cuenta-a-la-hora-de-instalar-savi.html"], ["2009/03/06/empanadas-mediterraneas/index.html", "/posts/2009/03/06/empanadas-mediterraneas.html"], ["2009/01/21/la-historia-de-python-cronologia-breve/index.html", "/posts/2009/01/21/la-historia-de-python-cronologia-breve.html"], ["2011/07/16/el-fin-de-la-infancia/index.html", "/posts/2011/07/16/el-fin-de-la-infancia.html"], ["2007/05/23/2da-jornada-python-en-santa-fe/index.html", "/posts/2007/05/23/2da-jornada-python-en-santa-fe.html"], ["2006/05/17/encuentre-las-7-diferencias/index.html", "/posts/2006/05/17/encuentre-las-7-diferencias.html"], ["2006/10/07/all-you-need-is-love/index.html", "/posts/2006/10/07/all-you-need-is-love.html"], ["2010/11/22/video-de-la-charla-entendiendo-decoradores-en-python/index.html", "/posts/2010/11/22/video-de-la-charla-entendiendo-decoradores-en-python.html"], ["2009/11/23/semana-de-la-seguridad/index.html", "/posts/2009/11/23/semana-de-la-seguridad.html"], ["2008/07/11/hoy-se-recibieron-mariano-y-nico/index.html", "/posts/2008/07/11/hoy-se-recibieron-mariano-y-nico.html"], ["2008/11/02/sql-debug-en-django/index.html", "/posts/2008/11/02/sql-debug-en-django.html"], ["2009/05/04/intercambio-de-valores-rapido-en-python/index.html", "/posts/2009/05/04/intercambio-de-valores-rapido-en-python.html"], ["2009/01/14/un-fin-de-semana-en-upg/index.html", "/posts/2009/01/14/un-fin-de-semana-en-upg.html"], ["2005/11/28/rivendel-lista-de-correos/index.html", "/posts/2005/11/28/rivendel-lista-de-correos.html"], ["2010/06/09/dormir-en-una-celda-langholmen-hotel-estocolmo/index.html", "/posts/2010/06/09/dormir-en-una-celda-langholmen-hotel-estocolmo.html"], ["2012/04/10/feria-de-publicaciones-independientes-el-domingo-en-santa-fe/index.html", "/posts/2012/04/10/feria-de-publicaciones-independientes-el-domingo-en-santa-fe.html"], ["2007/03/20/tarball-diario-de-life-fighter/index.html", "/posts/2007/03/20/tarball-diario-de-life-fighter.html"], ["2009/01/06/diseno-de-lenguajes/index.html", "/posts/2009/01/06/diseno-de-lenguajes.html"], ["2009/12/27/21-dias-aprende-a-programar-en-10-anos-es_ar/index.html", "/posts/2009/12/27/21-dias-aprende-a-programar-en-10-anos-es_ar.html"], ["2008/11/05/la-rata-lali/index.html", "/posts/2008/11/05/la-rata-lali.html"], ["2009/07/16/decoradores-en-python-ii/index.html", "/posts/2009/07/16/decoradores-en-python-ii.html"], ["2009/01/02/nosotros-los-programadores/index.html", "/posts/2009/01/02/nosotros-los-programadores.html"], ["2010/08/29/como-unir-videos-en-gnulinux/index.html", "/posts/2010/08/29/como-unir-videos-en-gnulinux.html"], ["2010/10/24/seminario-%e2%80%9cla-seguridad-en-el-proceso-de-desarrollo-de-software%e2%80%9d/index.html", "/posts/2010/10/24/seminario-ala-seguridad-en-el-proceso-de-desarrollo-de-softwarea.html"], ["2010/07/23/talk-taint-mode-for-python-via-a-library-video/index.html", "/posts/2010/07/23/talk-taint-mode-for-python-via-a-library-video.html"], ["2014/06/27/resena-de-xolopes-en-el-litoral/index.html", "/posts/2014/06/27/resena-de-xolopes-en-el-litoral.html"], ["2010/07/22/pilas-y-cola-en-python/index.html", "/posts/2010/07/22/pilas-y-cola-en-python.html"], ["2008/08/09/nuevo-numero-de-celular/index.html", "/posts/2008/08/09/nuevo-numero-de-celular.html"], ["2012/01/18/manana-no-hay-post-ni-blog/index.html", "/posts/2012/01/18/manana-no-hay-post-ni-blog.html"], ["2012/04/26/limpiar-wordpress-infectado/index.html", "/posts/2012/04/26/limpiar-wordpress-infectado.html"], ["2006/04/13/el-problema-de-los-formatos-cerrados/index.html", "/posts/2006/04/13/el-problema-de-los-formatos-cerrados.html"], ["2012/10/04/feria-del-libro-independiente-en-santa-fe/index.html", "/posts/2012/10/04/feria-del-libro-independiente-en-santa-fe.html"], ["2014/09/19/las-mujeres-de-bukowsky/index.html", "/posts/2014/09/19/las-mujeres-de-bukowsky.html"], ["2009/08/30/el-tutorial-de-python-en-espanol/index.html", "/posts/2009/08/30/el-tutorial-de-python-en-espanol.html"], ["2011/09/21/3-anos-despues-vuelvo-a-colaborar-con-un-comic-de-fraga/index.html", "/posts/2011/09/21/3-anos-despues-vuelvo-a-colaborar-con-un-comic-de-fraga.html"], ["2013/12/27/xolopes-68/index.html", "/posts/2013/12/27/xolopes-68.html"], ["2008/10/13/filosofos-y-lunas/index.html", "/posts/2008/10/13/filosofos-y-lunas.html"], ["2010/01/21/vacaciones-en-villa-gesell/index.html", "/posts/2010/01/21/vacaciones-en-villa-gesell.html"], ["2012/02/10/sonetos-parte-2/index.html", "/posts/2012/02/10/sonetos-parte-2.html"], ["2007/07/04/hunt-the-wumpus/index.html", "/posts/2007/07/04/hunt-the-wumpus.html"], ["2009/01/03/los-chicos-malos/index.html", "/posts/2009/01/03/los-chicos-malos.html"], ["2010/04/18/siempre-es-bueno-escuchar-a-richard/index.html", "/posts/2010/04/18/siempre-es-bueno-escuchar-a-richard.html"], ["2010/06/19/2da-semana-completa/index.html", "/posts/2010/06/19/2da-semana-completa.html"], ["2009/06/15/euler-5-python/index.html", "/posts/2009/06/15/euler-5-python.html"], ["2009/04/08/servidor-ssh-con-twisted/index.html", "/posts/2009/04/08/servidor-ssh-con-twisted.html"], ["2012/05/10/gobernados-por-la-fatalidad/index.html", "/posts/2012/05/10/gobernados-por-la-fatalidad.html"], ["2008/03/12/twisted-zombie-en-uptodown/index.html", "/posts/2008/03/12/twisted-zombie-en-uptodown.html"], ["2015/05/21/el-operario-jonatan-lipner/index.html", "/posts/2015/05/21/el-operario-jonatan-lipner.html"], ["2008/01/14/el-sol-desnudo/index.html", "/posts/2008/01/14/el-sol-desnudo.html"], ["2009/11/28/de-paseo-por-capital/index.html", "/posts/2009/11/28/de-paseo-por-capital.html"], ["2008/04/19/serpientes-y-rubies/index.html", "/posts/2008/04/19/serpientes-y-rubies.html"], ["2013/01/23/por-que-a-veces-me-confundo-y-escribo-por-que-en-lugar-de-porque/index.html", "/posts/2013/01/23/por-que-a-veces-me-confundo-y-escribo-por-que-en-lugar-de-porque.html"], ["2011/01/19/la-soledad-de-los-numeros-primos/index.html", "/posts/2011/01/19/la-soledad-de-los-numeros-primos.html"], ["2008/02/15/agua-mineral/index.html", "/posts/2008/02/15/agua-mineral.html"], ["2009/06/07/euler-3-python/index.html", "/posts/2009/06/07/euler-3-python.html"], ["2008/02/07/codigo-secreto-juego/index.html", "/posts/2008/02/07/codigo-secreto-juego.html"], ["2012/11/03/de-aca-a-la-china-y-la-autoproduccion-de-libritos/index.html", "/posts/2012/11/03/de-aca-a-la-china-y-la-autoproduccion-de-libritos.html"], ["2007/03/04/el-juego-del-verano/index.html", "/posts/2007/03/04/el-juego-del-verano.html"], ["2007/02/28/lista-circular-en-python/index.html", "/posts/2007/02/28/lista-circular-en-python.html"], ["2006/03/16/el-arte-de-python-fu-cinturon-blanco/index.html", "/posts/2006/03/16/el-arte-de-python-fu-cinturon-blanco.html"], ["2009/07/09/la-historia-de-python-el-problema-con-la-division-entre-enteros/index.html", "/posts/2009/07/09/la-historia-de-python-el-problema-con-la-division-entre-enteros.html"], ["2012/06/29/videos-sobre-el-entenado-de-saer/index.html", "/posts/2012/06/29/videos-sobre-el-entenado-de-saer.html"], ["2009/06/06/motorizado/index.html", "/posts/2009/06/06/motorizado.html"], ["2008/09/22/futbol-y-letras-3-para-crear/index.html", "/posts/2008/09/22/futbol-y-letras-3-para-crear.html"], ["2012/02/21/miopia/index.html", "/posts/2012/02/21/miopia.html"], ["2011/05/27/boleta-unica-en-santa-fe/index.html", "/posts/2011/05/27/boleta-unica-en-santa-fe.html"], ["2012/10/19/se-desperto/index.html", "/posts/2012/10/19/se-desperto.html"], ["2011/12/01/la-oficina-media/index.html", "/posts/2011/12/01/la-oficina-media.html"], ["2012/10/06/la-venganza-de-geller/index.html", "/posts/2012/10/06/la-venganza-de-geller.html"], ["2012/12/12/microcuentos/index.html", "/posts/2012/12/12/microcuentos.html"], ["2009/05/11/nuevo-perrito/index.html", "/posts/2009/05/11/nuevo-perrito.html"], ["2009/01/05/codigo-re-editable/index.html", "/posts/2009/01/05/codigo-re-editable.html"], ["2013/12/19/xolopes-7/index.html", "/posts/2013/12/19/xolopes-7.html"], ["2007/11/23/musica-libre/index.html", "/posts/2007/11/23/musica-libre.html"], ["2009/05/21/budin-de-remolacha-y-nuez/index.html", "/posts/2009/05/21/budin-de-remolacha-y-nuez.html"], ["2014/01/26/twitter-dejar-de-seguir-a-los-que-no-me-siguen/index.html", "/posts/2014/01/26/twitter-dejar-de-seguir-a-los-que-no-me-siguen.html"], ["2010/05/02/8-de-mayo-python-day-en-rafaela/index.html", "/posts/2010/05/02/8-de-mayo-python-day-en-rafaela.html"], ["2008/05/14/workaround-para-el-bug-7233-de-django/index.html", "/posts/2008/05/14/workaround-para-el-bug-7233-de-django.html"], ["2007/08/28/log-de-tutorial-sobre-empaquetado-para-debianubuntu/index.html", "/posts/2007/08/28/log-de-tutorial-sobre-empaquetado-para-debianubuntu.html"], ["2007/05/01/smarter-n-puzzle/index.html", "/posts/2007/05/01/smarter-n-puzzle.html"], ["2007/03/29/sobre-el-nuevo-borrador-de-gpl-v3/index.html", "/posts/2007/03/29/sobre-el-nuevo-borrador-de-gpl-v3.html"], ["2010/11/28/video-de-la-charla-sobre-sysadmins-de-cballard-en-act_as_rubylit-2010/index.html", "/posts/2010/11/28/video-de-la-charla-sobre-sysadmins-de-cballard-en-act_as_rubylit-2010.html"], ["2010/12/21/smartphones/index.html", "/posts/2010/12/21/smartphones.html"], ["2007/04/06/la-matrix-se-colgo/index.html", "/posts/2007/04/06/la-matrix-se-colgo.html"], ["2012/05/01/impreso-en-argentina-2/index.html", "/posts/2012/05/01/impreso-en-argentina-2.html"], ["2007/12/01/youtube-user-google/index.html", "/posts/2007/12/01/youtube-user-google.html"], ["2010/12/20/publique-un-libro-de-cuentos/index.html", "/posts/2010/12/20/publique-un-libro-de-cuentos.html"], ["2009/06/16/fotos-campo/index.html", "/posts/2009/06/16/fotos-campo.html"], ["2007/05/28/un-fin-de-semana-resfriado/index.html", "/posts/2007/05/28/un-fin-de-semana-resfriado.html"], ["2011/10/31/debate-sobre-voto-electronico-en-santa-fe/index.html", "/posts/2011/10/31/debate-sobre-voto-electronico-en-santa-fe.html"], ["2008/05/22/bienvenido-pablo/index.html", "/posts/2008/05/22/bienvenido-pablo.html"], ["2013/09/03/mis-columnas-preferidas-de-pedro-mairal-en-perfil/index.html", "/posts/2013/09/03/mis-columnas-preferidas-de-pedro-mairal-en-perfil.html"], ["2015/01/12/restos-del-pasado-presente/index.html", "/posts/2015/01/12/restos-del-pasado-presente.html"], ["2008/08/30/saliendo-para-brasil/index.html", "/posts/2008/08/30/saliendo-para-brasil.html"], ["2011/05/31/leyendo-a-dolina/index.html", "/posts/2011/05/31/leyendo-a-dolina.html"], ["2009/04/06/manana-voto-electronico-en-santa-fe/index.html", "/posts/2009/04/06/manana-voto-electronico-en-santa-fe.html"], ["2009/06/28/sorry-por-el-spam/index.html", "/posts/2009/06/28/sorry-por-el-spam.html"], ["2008/10/13/listado-de-herramientas-de-seguridad/index.html", "/posts/2008/10/13/listado-de-herramientas-de-seguridad.html"], ["2006/05/07/microoft-insta-ayuda-a-las-personas-a-decidirse-por-gnulinux/index.html", "/posts/2006/05/07/microoft-insta-ayuda-a-las-personas-a-decidirse-por-gnulinux.html"], ["2008/06/08/un-meta-chiste/index.html", "/posts/2008/06/08/un-meta-chiste.html"], ["2010/02/01/novelas-que-lei-en-enero2010/index.html", "/posts/2010/02/01/novelas-que-lei-en-enero2010.html"], ["2005/10/05/compilando-el-primer-ping/index.html", "/posts/2005/10/05/compilando-el-primer-ping.html"], ["2009/03/09/3-features-de-sqlite-que-no-conocia/index.html", "/posts/2009/03/09/3-features-de-sqlite-que-no-conocia.html"], ["2007/09/28/harry-potter-y-los-lenguajes-de-programacion/index.html", "/posts/2007/09/28/harry-potter-y-los-lenguajes-de-programacion.html"], ["2007/11/13/ejemplos-de-ply/index.html", "/posts/2007/11/13/ejemplos-de-ply.html"], ["2009/12/24/feliz-navidad/index.html", "/posts/2009/12/24/feliz-navidad.html"], ["2012/05/17/en-santa-fe-y-alrededores-hay-fanaticos-hardcore-de-orsai/index.html", "/posts/2012/05/17/en-santa-fe-y-alrededores-hay-fanaticos-hardcore-de-orsai.html"], ["2011/01/04/tron/index.html", "/posts/2011/01/04/tron.html"], ["2014/04/23/xolopes-impreso-y-a-la-venta/index.html", "/posts/2014/04/23/xolopes-impreso-y-a-la-venta.html"], ["2006/11/15/wp-print-en-espanol/index.html", "/posts/2006/11/15/wp-print-en-espanol.html"], ["2006/01/14/py2html/index.html", "/posts/2006/01/14/py2html.html"], ["2006/06/22/todo-el-material-de-python-santa-fe/index.html", "/posts/2006/06/22/todo-el-material-de-python-santa-fe.html"], ["2007/04/21/guantanamero-by-rms/index.html", "/posts/2007/04/21/guantanamero-by-rms.html"], ["2008/12/13/colores-personalizados-en-openoffice/index.html", "/posts/2008/12/13/colores-personalizados-en-openoffice.html"], ["2006/06/04/el-zen-de-python/index.html", "/posts/2006/06/04/el-zen-de-python.html"], ["2014/04/14/fotos-de-cuba-buscando-un-libro-de-analisis-matematico-en-la-biblioteca-de-la-universidad-de-la-habana/index.html", "/posts/2014/04/14/fotos-de-cuba-buscando-un-libro-de-analisis-matematico-en-la-biblioteca-de-la-universidad-de-la-habana.html"], ["libros/cuentos3/index.html", "/stories/libros/cuentos3.html"], ["2007/04/10/naaaa/index.html", "/posts/2007/04/10/naaaa.html"], ["2011/01/03/segunda-edicion/index.html", "/posts/2011/01/03/segunda-edicion.html"], ["2013/12/22/xolopes-21/index.html", "/posts/2013/12/22/xolopes-21.html"], ["2009/11/14/algunas-fotos-del-34%c2%b0-acto-de-colacion-de-grado/index.html", "/posts/2009/11/14/algunas-fotos-del-34adeg-acto-de-colacion-de-grado.html"], ["2010/09/14/cambiando-el-formato-de-los-logs-en-twisted/index.html", "/posts/2010/09/14/cambiando-el-formato-de-los-logs-en-twisted.html"], ["2009/12/14/fotos-del-paque-urquiza-parana/index.html", "/posts/2009/12/14/fotos-del-paque-urquiza-parana.html"], ["2006/08/14/pythonday-en-cordoba/index.html", "/posts/2006/08/14/pythonday-en-cordoba.html"], ["2013/12/24/25/index.html", "/posts/2013/12/24/25.html"], ["2012/12/01/me-dedicaron-un-comic/index.html", "/posts/2012/12/01/me-dedicaron-un-comic.html"], ["2010/12/13/mantra-de-la-semana-know-your-tools/index.html", "/posts/2010/12/13/mantra-de-la-semana-know-your-tools.html"], ["2013/09/18/ejemplares-a-la-venta/index.html", "/posts/2013/09/18/ejemplares-a-la-venta.html"], ["2006/08/22/creando-plug-ins-para-gimp-con-python-charla/index.html", "/posts/2006/08/22/creando-plug-ins-para-gimp-con-python-charla.html"], ["2014/04/15/los-diarios-secretos-de-sigmundo/index.html", "/posts/2014/04/15/los-diarios-secretos-de-sigmundo.html"], ["2012/01/22/the-girl-with-the-dragon-tattoo-bonus-track/index.html", "/posts/2012/01/22/the-girl-with-the-dragon-tattoo-bonus-track.html"], ["2008/06/28/usando-django-notification/index.html", "/posts/2008/06/28/usando-django-notification.html"], ["2006/08/30/fito-paez-%e2%80%9cyo-cuando-tenia-15-anos-compraba-un-disco-y-grababa-10%e2%80%9d/index.html", "/posts/2006/08/30/fito-paez-ayo-cuando-tenia-15-anos-compraba-un-disco-y-grababa-10a.html"], ["2013/11/07/se-desperto-editado/index.html", "/posts/2013/11/07/se-desperto-editado.html"], ["2007/10/10/smalltalks-2007/index.html", "/posts/2007/10/10/smalltalks-2007.html"], ["2010/08/15/lo-que-todo-programdor-deberia-saber-sobre/index.html", "/posts/2010/08/15/lo-que-todo-programdor-deberia-saber-sobre.html"], ["2010/08/24/un-servidor-web-con-pocas-lineas-de-python/index.html", "/posts/2010/08/24/un-servidor-web-con-pocas-lineas-de-python.html"], ["2012/10/12/relei-el-juego-del-angel/index.html", "/posts/2012/10/12/relei-el-juego-del-angel.html"], ["2008/07/11/decoradores-en-python-i/index.html", "/posts/2008/07/11/decoradores-en-python-i.html"], ["2009/09/18/euler-16/index.html", "/posts/2009/09/18/euler-16.html"], ["2007/12/30/la-cultura-es/index.html", "/posts/2007/12/30/la-cultura-es.html"], ["taint/index.html", "/stories/taint.html"], ["2008/10/28/recomendaciones-al-programar-en-python/index.html", "/posts/2008/10/28/recomendaciones-al-programar-en-python.html"], ["2010/11/08/los-hombres-que-no-amaban-a-las-mujeres-una-novela-sueca/index.html", "/posts/2010/11/08/los-hombres-que-no-amaban-a-las-mujeres-una-novela-sueca.html"], ["2010/06/26/midsummer-2010/index.html", "/posts/2010/06/26/midsummer-2010.html"], ["2006/06/06/proximos-eventos-de-la-comunidad/index.html", "/posts/2006/06/06/proximos-eventos-de-la-comunidad.html"], ["2008/09/28/el-juego-mas-votado-de-pyweek-7/index.html", "/posts/2008/09/28/el-juego-mas-votado-de-pyweek-7.html"], ["2007/07/17/herramientas-para-la-construccion-cooperativa-a-traves-de-internet/index.html", "/posts/2007/07/17/herramientas-para-la-construccion-cooperativa-a-traves-de-internet.html"], ["2009/06/18/euler-7-python/index.html", "/posts/2009/06/18/euler-7-python.html"], ["2014/09/09/ejemplares-de-santa-furia-disponibles-para-la-venta/index.html", "/posts/2014/09/09/ejemplares-de-santa-furia-disponibles-para-la-venta.html"], ["2008/08/02/como-un-viejo-rock-n-roll/index.html", "/posts/2008/08/02/como-un-viejo-rock-n-roll.html"], ["2014/12/12/ultima-reunion-de-rubylit-del-2014/index.html", "/posts/2014/12/12/ultima-reunion-de-rubylit-del-2014.html"], ["2010/10/13/entendiendo-args-y-kwargs-en-python/index.html", "/posts/2010/10/13/entendiendo-args-y-kwargs-en-python.html"], ["2009/09/07/charla-taint-mode-en-python/index.html", "/posts/2009/09/07/charla-taint-mode-en-python.html"], ["2007/08/08/saliendo-para-las-7mas-jornadas-regionales-de-software-libre/index.html", "/posts/2007/08/08/saliendo-para-las-7mas-jornadas-regionales-de-software-libre.html"], ["2013/06/15/nuevo-libro-artesanal-leer-bajo-receta/index.html", "/posts/2013/06/15/nuevo-libro-artesanal-leer-bajo-receta.html"], ["2014/09/08/taller-de-anecdotas-mejoradas-de-orsai-en-rosario/index.html", "/posts/2014/09/08/taller-de-anecdotas-mejoradas-de-orsai-en-rosario.html"], ["2007/01/23/canciones-de-soledad/index.html", "/posts/2007/01/23/canciones-de-soledad.html"], ["2010/08/05/coloreando-codigo-fuente-en-wordpress/index.html", "/posts/2010/08/05/coloreando-codigo-fuente-en-wordpress.html"], ["2011/06/23/orsai-1-pdf/index.html", "/posts/2011/06/23/orsai-1-pdf.html"], ["2008/09/02/fotos-de-brasil/index.html", "/posts/2008/09/02/fotos-de-brasil.html"], ["2011/11/24/cuento-para-chicos-el-recreo-mas-largo-de-la-historia/index.html", "/posts/2011/11/24/cuento-para-chicos-el-recreo-mas-largo-de-la-historia.html"], ["2011/09/24/lighting-talks-en-pyconar-2011-dia-2/index.html", "/posts/2011/09/24/lighting-talks-en-pyconar-2011-dia-2.html"], ["2015/07/19/primera-experiencia-con-thewalnut-io/index.html", "/posts/2015/07/19/primera-experiencia-con-thewalnut-io.html"], ["2013/02/08/yo-por-leandro-rojas/index.html", "/posts/2013/02/08/yo-por-leandro-rojas.html"], ["2006/07/19/escaneando-la-blogosfera/index.html", "/posts/2006/07/19/escaneando-la-blogosfera.html"], ["2010/08/20/la-ultima-leccion-libro/index.html", "/posts/2010/08/20/la-ultima-leccion-libro.html"], ["2014/08/15/middle-office/index.html", "/posts/2014/08/15/middle-office.html"], ["2006/05/29/fermat-vs-pythagoras/index.html", "/posts/2006/05/29/fermat-vs-pythagoras.html"], ["2005/09/14/paradigmas-de-programacion/index.html", "/posts/2005/09/14/paradigmas-de-programacion.html"], ["2008/04/10/goodbye-clarke-hello-asimov/index.html", "/posts/2008/04/10/goodbye-clarke-hello-asimov.html"], ["2015/05/12/videos-de-felisa-2015/index.html", "/posts/2015/05/12/videos-de-felisa-2015.html"], ["2006/09/21/feliz-dia-del-estudiante/index.html", "/posts/2006/09/21/feliz-dia-del-estudiante.html"], ["2012/04/06/luna-de-miel/index.html", "/posts/2012/04/06/luna-de-miel.html"], ["2014/07/16/paredon-un-cuento-de-futbol/index.html", "/posts/2014/07/16/paredon-un-cuento-de-futbol.html"], ["tienda-virtual/index.html", "/stories/tienda-virtual.html"], ["2011/02/03/the-power-of-love/index.html", "/posts/2011/02/03/the-power-of-love.html"], ["2008/04/09/pyweek-6/index.html", "/posts/2008/04/09/pyweek-6.html"], ["2006/01/27/python-modeel/index.html", "/posts/2006/01/27/python-modeel.html"], ["2011/04/11/pyday-en-cordoba/index.html", "/posts/2011/04/11/pyday-en-cordoba.html"], ["2008/08/06/archives/index.html", "/posts/2008/08/06/archives.html"], ["2008/11/22/mi-humor-en-axxon/index.html", "/posts/2008/11/22/mi-humor-en-axxon.html"], ["2012/04/14/un-microcuento-mio-llevado-al-comic/index.html", "/posts/2012/04/14/un-microcuento-mio-llevado-al-comic.html"], ["2014/06/16/nuevo-libro/index.html", "/posts/2014/06/16/nuevo-libro.html"], ["2008/11/30/dulce-de-mora/index.html", "/posts/2008/11/30/dulce-de-mora.html"], ["2011/01/05/la-chica-que-sonaba-con-un-acerilla-y-un-bidon-de-gasolina/index.html", "/posts/2011/01/05/la-chica-que-sonaba-con-un-acerilla-y-un-bidon-de-gasolina.html"], ["2005/09/06/fourier-2-new-feature/index.html", "/posts/2005/09/06/fourier-2-new-feature.html"], ["2015/03/23/el-pelo-en-el-jabon-remasterizado/index.html", "/posts/2015/03/23/el-pelo-en-el-jabon-remasterizado.html"], ["2008/10/24/python-en-santa-fe-declarado-de-interes-educativo-provincial/index.html", "/posts/2008/10/24/python-en-santa-fe-declarado-de-interes-educativo-provincial.html"], ["2008/10/14/sentados-bajo-la-lluvia/index.html", "/posts/2008/10/14/sentados-bajo-la-lluvia.html"], ["2009/07/15/galletitas-de-avena-y-manzana/index.html", "/posts/2009/07/15/galletitas-de-avena-y-manzana.html"], ["2012/05/06/que-comemos-hoy-cuento/index.html", "/posts/2012/05/06/que-comemos-hoy-cuento.html"], ["2012/09/15/matar-a-borges/index.html", "/posts/2012/09/15/matar-a-borges.html"], ["2008/10/06/streaming-de-dato-en-django/index.html", "/posts/2008/10/06/streaming-de-dato-en-django.html"], ["2014/01/02/libros-que-lei-o-intente-leer-en-la-ultima-parte-de-2013/index.html", "/posts/2014/01/02/libros-que-lei-o-intente-leer-en-la-ultima-parte-de-2013.html"], ["2012/10/19/version-digital-de-los-caballeros-de-la-rosa/index.html", "/posts/2012/10/19/version-digital-de-los-caballeros-de-la-rosa.html"], ["2009/01/20/la-historia-de-python-introduccion-y-repaso/index.html", "/posts/2009/01/20/la-historia-de-python-introduccion-y-repaso.html"], ["2011/09/18/razones-para-ir-a-pyconar-2011/index.html", "/posts/2011/09/18/razones-para-ir-a-pyconar-2011.html"], ["2009/04/30/la-historia-de-python-como-todo-se-convirtio-en-sentencias-ejecutables/index.html", "/posts/2009/04/30/la-historia-de-python-como-todo-se-convirtio-en-sentencias-ejecutables.html"], ["2009/02/15/herramientas/index.html", "/posts/2009/02/15/herramientas.html"], ["2009/06/16/euler-6-python/index.html", "/posts/2009/06/16/euler-6-python.html"], ["2015/06/18/jugando-con-los-datos-del-escrutinio-provisorio/index.html", "/posts/2015/06/18/jugando-con-los-datos-del-escrutinio-provisorio.html"], ["2012/04/15/generar-un-video-a-partir-de-miles-de-fotos/index.html", "/posts/2012/04/15/generar-un-video-a-partir-de-miles-de-fotos.html"], ["2010/12/01/videos-de-las-charlas-en-junin/index.html", "/posts/2010/12/01/videos-de-las-charlas-en-junin.html"], ["2014/08/18/aprendiendo-ruby-desde-python/index.html", "/posts/2014/08/18/aprendiendo-ruby-desde-python.html"], ["2009/04/17/guerra-y-ta-te-ti/index.html", "/posts/2009/04/17/guerra-y-ta-te-ti.html"], ["2007/03/02/problemas-con-la-version-de-wxpython-al-intentar-iniciar-spe/index.html", "/posts/2007/03/02/problemas-con-la-version-de-wxpython-al-intentar-iniciar-spe.html"], ["2006/04/05/no-a-la-alianza-por-la-educacion/index.html", "/posts/2006/04/05/no-a-la-alianza-por-la-educacion.html"], ["2011/07/30/borges-en-zafon/index.html", "/posts/2011/07/30/borges-en-zafon.html"], ["2012/05/03/el-chiri-de-orsai-en-santa-fe/index.html", "/posts/2012/05/03/el-chiri-de-orsai-en-santa-fe.html"], ["2009/01/04/aprender-a-programar/index.html", "/posts/2009/01/04/aprender-a-programar.html"], ["2008/01/04/reservar-harry-potter-7-en-castella-santa-fe/index.html", "/posts/2008/01/04/reservar-harry-potter-7-en-castella-santa-fe.html"], ["2009/01/11/por-que-nos-gusta-python/index.html", "/posts/2009/01/11/por-que-nos-gusta-python.html"], ["2010/11/29/llaveros-con-memoria-ram/index.html", "/posts/2010/11/29/llaveros-con-memoria-ram.html"], ["2007/04/03/mira-esta-pelicula/index.html", "/posts/2007/04/03/mira-esta-pelicula.html"], ["2006/08/23/fin-de-semana-en-cordoba-mi-seleccion-de-fotos/index.html", "/posts/2006/08/23/fin-de-semana-en-cordoba-mi-seleccion-de-fotos.html"], ["2009/01/07/automoviles-y-programas/index.html", "/posts/2009/01/07/automoviles-y-programas.html"], ["2012/01/24/relatos-de-zafon/index.html", "/posts/2012/01/24/relatos-de-zafon.html"], ["2011/05/25/renault-sandero/index.html", "/posts/2011/05/25/renault-sandero.html"], ["2013/01/20/tesis-sobre-un-homicidio/index.html", "/posts/2013/01/20/tesis-sobre-un-homicidio.html"], ["2010/06/15/acuario-en-universeum/index.html", "/posts/2010/06/15/acuario-en-universeum.html"], ["2007/05/01/clausuras-en-python/index.html", "/posts/2007/05/01/clausuras-en-python.html"], ["2008/10/23/generar-diagramas-de-clases-a-partir-de-modelos-de-django/index.html", "/posts/2008/10/23/generar-diagramas-de-clases-a-partir-de-modelos-de-django.html"], ["2010/04/06/la-historia-de-python-el-gran-o-enorme-renombrado/index.html", "/posts/2010/04/06/la-historia-de-python-el-gran-o-enorme-renombrado.html"], ["2012/10/22/fotos-de-flia-santa-fe-2012/index.html", "/posts/2012/10/22/fotos-de-flia-santa-fe-2012.html"], ["2009/08/02/una-gran-oportunidad-de-conocer-python/index.html", "/posts/2009/08/02/una-gran-oportunidad-de-conocer-python.html"], ["2013/03/18/221163/index.html", "/posts/2013/03/18/221163.html"], ["2008/01/19/una-experiencia-en-pythonbugday/index.html", "/posts/2008/01/19/una-experiencia-en-pythonbugday.html"], ["2008/08/18/fotografiando-desde-el-camino/index.html", "/posts/2008/08/18/fotografiando-desde-el-camino.html"], ["2015/07/26/glider-gun-en-thewalnut-io/index.html", "/posts/2015/07/26/glider-gun-en-thewalnut-io.html"], ["2006/07/29/2-nuevos-plug-ins-en-mi-wp/index.html", "/posts/2006/07/29/2-nuevos-plug-ins-en-mi-wp.html"], ["2010/10/16/mis-charlas-en-pyconar2010/index.html", "/posts/2010/10/16/mis-charlas-en-pyconar2010.html"], ["2006/04/03/kit-de-plug-ins-para-generar-diagramas-de-constelaciones-con-gimp/index.html", "/posts/2006/04/03/kit-de-plug-ins-para-generar-diagramas-de-constelaciones-con-gimp.html"], ["2006/03/17/plug-in-para-gimp-que-genera-constelaciones-psk/index.html", "/posts/2006/03/17/plug-in-para-gimp-que-genera-constelaciones-psk.html"], ["2012/05/07/perigeo/index.html", "/posts/2012/05/07/perigeo.html"], ["2014/09/09/el-ultimo-capitulo-de-una-muchacha-muy-bella/index.html", "/posts/2014/09/09/el-ultimo-capitulo-de-una-muchacha-muy-bella.html"], ["2012/06/15/a-imprenta/index.html", "/posts/2012/06/15/a-imprenta.html"], ["2010/06/28/location-update-freiburg-alemania/index.html", "/posts/2010/06/28/location-update-freiburg-alemania.html"], ["2014/09/17/sobre-la-existencia-de-los-fantasmas-en-yerba-6/index.html", "/posts/2014/09/17/sobre-la-existencia-de-los-fantasmas-en-yerba-6.html"], ["2007/03/10/revolution-os-en-i-sat/index.html", "/posts/2007/03/10/revolution-os-en-i-sat.html"], ["2010/01/25/celular-cuento/index.html", "/posts/2010/01/25/celular-cuento.html"], ["2007/08/29/irc2htmlpy/index.html", "/posts/2007/08/29/irc2htmlpy.html"], ["2010/09/23/reflotando-mytwitgroup/index.html", "/posts/2010/09/23/reflotando-mytwitgroup.html"], ["2014/10/31/se-viene-la-pyconar-2014/index.html", "/posts/2014/10/31/se-viene-la-pyconar-2014.html"], ["2008/10/30/diagrama-de-capas-de-django/index.html", "/posts/2008/10/30/diagrama-de-capas-de-django.html"], ["2006/11/28/1%c2%aa-experiencia-xp/index.html", "/posts/2006/11/28/1aa-experiencia-xp.html"], ["2011/07/08/el-canto-de-clementina-cuento/index.html", "/posts/2011/07/08/el-canto-de-clementina-cuento.html"], ["2007/03/13/un-nuevo-planeta/index.html", "/posts/2007/03/13/un-nuevo-planeta.html"], ["2006/04/15/opensourceparkingcom/index.html", "/posts/2006/04/15/opensourceparkingcom.html"], ["2012/02/02/mrs-robinson-no-es-de-los-beatles/index.html", "/posts/2012/02/02/mrs-robinson-no-es-de-los-beatles.html"], ["2012/02/05/dulce-de-higo-2/index.html", "/posts/2012/02/05/dulce-de-higo-2.html"], ["2010/08/29/dejar-de-revisionar-un-archivo-sin-borrarlo-en-svn/index.html", "/posts/2010/08/29/dejar-de-revisionar-un-archivo-sin-borrarlo-en-svn.html"], ["2009/06/04/euler-2-python/index.html", "/posts/2009/06/04/euler-2-python.html"], ["2010/09/18/torta-de-zanahoria/index.html", "/posts/2010/09/18/torta-de-zanahoria.html"], ["2014/09/16/presentacion-de-la-novela-xolopes-video/index.html", "/posts/2014/09/16/presentacion-de-la-novela-xolopes-video.html"], ["2015/02/15/lecturas-en-la-presentacion-del-libro-pulover/index.html", "/posts/2015/02/15/lecturas-en-la-presentacion-del-libro-pulover.html"], ["2015/06/29/soledad-en-santa-fe-vivireshoy/index.html", "/posts/2015/06/29/soledad-en-santa-fe-vivireshoy.html"], ["2013/03/11/appinventor/index.html", "/posts/2013/03/11/appinventor.html"], ["2007/06/12/firefox-search-engine-en-5-minutos/index.html", "/posts/2007/06/12/firefox-search-engine-en-5-minutos.html"], ["2012/08/25/el-enfoque-en-la-novela/index.html", "/posts/2012/08/25/el-enfoque-en-la-novela.html"], ["libros/cuentos/index.html", "/stories/libros/cuentos.html"], ["2015/06/25/libros-que-lei-mientras-estudiaba-swift/index.html", "/posts/2015/06/25/libros-que-lei-mientras-estudiaba-swift.html"], ["2007/04/08/rocky-vi/index.html", "/posts/2007/04/08/rocky-vi.html"], ["2006/03/15/%c2%bftomamos-mate/index.html", "/posts/2006/03/15/atomamos-mate.html"], ["2011/05/25/el-caballo-y-su-nino/index.html", "/posts/2011/05/25/el-caballo-y-su-nino.html"], ["juanjo/index.html", "/stories/juanjo.html"], ["2006/09/04/gnulinux-en-oro-verde/index.html", "/posts/2006/09/04/gnulinux-en-oro-verde.html"], ["2005/09/24/el-capitan-julio-cesar/index.html", "/posts/2005/09/24/el-capitan-julio-cesar.html"], ["2011/02/08/unicode-en-el-codigo-fuente/index.html", "/posts/2011/02/08/unicode-en-el-codigo-fuente.html"], ["2012/02/25/me-caso/index.html", "/posts/2012/02/25/me-caso.html"], ["2009/07/12/9-de-julio-en-el-parque-garay/index.html", "/posts/2009/07/12/9-de-julio-en-el-parque-garay.html"], ["2010/06/21/videos-del-paseo-por-el-archipielago-de-gotemburgo/index.html", "/posts/2010/06/21/videos-del-paseo-por-el-archipielago-de-gotemburgo.html"], ["2008/09/17/cecilia-music-game/index.html", "/posts/2008/09/17/cecilia-music-game.html"], ["2014/01/05/el-mapa-de-xolopes/index.html", "/posts/2014/01/05/el-mapa-de-xolopes.html"], ["2006/05/16/contribucion-recibida-para-la-pagina-de-paradigmas/index.html", "/posts/2006/05/16/contribucion-recibida-para-la-pagina-de-paradigmas.html"], ["2006/06/20/segui-el-mundial-desde-tu-firefox/index.html", "/posts/2006/06/20/segui-el-mundial-desde-tu-firefox.html"], ["2010/12/24/receta-pan-dulce/index.html", "/posts/2010/12/24/receta-pan-dulce.html"], ["2012/08/16/caperucita-roja/index.html", "/posts/2012/08/16/caperucita-roja.html"], ["2014/06/22/presentacion-de-santa-furia-en-uhlala-cafe/index.html", "/posts/2014/06/22/presentacion-de-santa-furia-en-uhlala-cafe.html"], ["2006/09/22/tener-una-menta-abierta/index.html", "/posts/2006/09/22/tener-una-menta-abierta.html"], ["2009/04/20/la-historia-de-python-clases-definidas-por-los-usuarios/index.html", "/posts/2009/04/20/la-historia-de-python-clases-definidas-por-los-usuarios.html"], ["2012/01/12/mis-textos-preferidos-de-hernan-casciari/index.html", "/posts/2012/01/12/mis-textos-preferidos-de-hernan-casciari.html"], ["2009/10/27/5tas-jornadas-de-software-libre-de-junin/index.html", "/posts/2009/10/27/5tas-jornadas-de-software-libre-de-junin.html"], ["2014/03/08/el-primer-romantico-un-cuento-por-el-dia-de-la-mujer/index.html", "/posts/2014/03/08/el-primer-romantico-un-cuento-por-el-dia-de-la-mujer.html"], ["2010/12/15/just-for-fun/index.html", "/posts/2010/12/15/just-for-fun.html"], ["2007/07/11/primer-proyeccion-de-la-orden-del-fenix-en-santa-fe/index.html", "/posts/2007/07/11/primer-proyeccion-de-la-orden-del-fenix-en-santa-fe.html"], ["2011/07/03/regalos-en-la-era-de-internet/index.html", "/posts/2011/07/03/regalos-en-la-era-de-internet.html"], ["libros/cuentos2/index.html", "/stories/libros/cuentos2.html"], ["2012/02/05/higos-en-almibar/index.html", "/posts/2012/02/05/higos-en-almibar.html"], ["2008/12/23/ingenieria-y-cumple-24/index.html", "/posts/2008/12/23/ingenieria-y-cumple-24.html"], ["2014/12/19/reactive-el-bot-jjsaer/index.html", "/posts/2014/12/19/reactive-el-bot-jjsaer.html"], ["2015/03/31/6-nuevos-libros-de-diego-arbit/index.html", "/posts/2015/03/31/6-nuevos-libros-de-diego-arbit.html"], ["2011/08/01/nieve-en-santa-fe/index.html", "/posts/2011/08/01/nieve-en-santa-fe.html"], ["2007/07/02/cuentos-cortos-pero-muy-cortos/index.html", "/posts/2007/07/02/cuentos-cortos-pero-muy-cortos.html"], ["2006/01/07/bases-en-python/index.html", "/posts/2006/01/07/bases-en-python.html"], ["2010/01/08/generacion-espontanea-de-codigo/index.html", "/posts/2010/01/08/generacion-espontanea-de-codigo.html"], ["2014/04/11/los-alucinantes-viajes-en-el-tiempo-de-los-ee-uu/index.html", "/posts/2014/04/11/los-alucinantes-viajes-en-el-tiempo-de-los-ee-uu.html"], ["2014/12/16/nueva-edicion-de-santa-furia/index.html", "/posts/2014/12/16/nueva-edicion-de-santa-furia.html"], ["2012/01/13/entre-a-la-farmacia-luz-y-fuerza/index.html", "/posts/2012/01/13/entre-a-la-farmacia-luz-y-fuerza.html"], ["2008/04/28/borrar-muchas-lineas-con-vim/index.html", "/posts/2008/04/28/borrar-muchas-lineas-con-vim.html"], ["2009/02/23/la-historia-de-python-historia-personal-parte-2-cnri-y-mas/index.html", "/posts/2009/02/23/la-historia-de-python-historia-personal-parte-2-cnri-y-mas.html"], ["2006/05/27/mi-nuevo-juguete/index.html", "/posts/2006/05/27/mi-nuevo-juguete.html"], ["2008/06/12/soporte-unicode-para-pyrtf-ng/index.html", "/posts/2008/06/12/soporte-unicode-para-pyrtf-ng.html"], ["2010/06/24/owasp-app-sec-2010-social/index.html", "/posts/2010/06/24/owasp-app-sec-2010-social.html"], ["2014/02/18/lenguajes-para-trabajar-y-lenguajes-para-estudiar/index.html", "/posts/2014/02/18/lenguajes-para-trabajar-y-lenguajes-para-estudiar.html"], ["2012/04/18/la-justificacion-de-los-cuentos-cortos/index.html", "/posts/2012/04/18/la-justificacion-de-los-cuentos-cortos.html"], ["2011/05/24/la-ceremonia-del-te/index.html", "/posts/2011/05/24/la-ceremonia-del-te.html"], ["2008/12/26/meta-analogia/index.html", "/posts/2008/12/26/meta-analogia.html"], ["2011/09/23/lighting-talks-en-pyconar-2011/index.html", "/posts/2011/09/23/lighting-talks-en-pyconar-2011.html"], ["2014/09/23/1er-slam-en-santa-fe/index.html", "/posts/2014/09/23/1er-slam-en-santa-fe.html"], ["2012/08/18/simple-template-latex-para-escribir-una-novela/index.html", "/posts/2012/08/18/simple-template-latex-para-escribir-una-novela.html"], ["2011/04/20/edicion-digital-de-la-maquina-de-los-cuentos/index.html", "/posts/2011/04/20/edicion-digital-de-la-maquina-de-los-cuentos.html"], ["2008/03/17/destapando-las-canerias-de-planet-planet/index.html", "/posts/2008/03/17/destapando-las-canerias-de-planet-planet.html"], ["2006/09/19/alfabeto-calculadora/index.html", "/posts/2006/09/19/alfabeto-calculadora.html"], ["2006/11/14/java-ahora-libre/index.html", "/posts/2006/11/14/java-ahora-libre.html"], ["2009/01/26/fotos-de-enero-en-santa-fe/index.html", "/posts/2009/01/26/fotos-de-enero-en-santa-fe.html"], ["2012/01/19/mala-postal-de-santa-fe-1/index.html", "/posts/2012/01/19/mala-postal-de-santa-fe-1.html"], ["2006/01/29/historia-de-trenes/index.html", "/posts/2006/01/29/historia-de-trenes.html"], ["2012/08/29/28-de-agosto/index.html", "/posts/2012/08/29/28-de-agosto.html"], ["2011/12/13/feriantes/index.html", "/posts/2011/12/13/feriantes.html"], ["2007/11/22/free-fonts/index.html", "/posts/2007/11/22/free-fonts.html"], ["2006/05/25/3n1/index.html", "/posts/2006/05/25/3n1.html"], ["2013/01/05/saer-en-bits/index.html", "/posts/2013/01/05/saer-en-bits.html"], ["2012/05/01/26-personas-para-salvar-al-mundo/index.html", "/posts/2012/05/01/26-personas-para-salvar-al-mundo.html"], ["2006/04/22/organizando-python-santa-fe-2006/index.html", "/posts/2006/04/22/organizando-python-santa-fe-2006.html"], ["2015/06/25/screensaver-ninja/index.html", "/posts/2015/06/25/screensaver-ninja.html"], ["2008/09/26/preguntas-y-respuestas/index.html", "/posts/2008/09/26/preguntas-y-respuestas.html"], ["2009/02/16/yo-y-el-futbol/index.html", "/posts/2009/02/16/yo-y-el-futbol.html"], ["2010/04/01/la-historia-de-python-modulos-cargados-dinamicamente/index.html", "/posts/2010/04/01/la-historia-de-python-modulos-cargados-dinamicamente.html"], ["2014/11/20/la-prueba-del-dulce-de-leche-un-cuento-regalo-de-cumpleanos-para-mi-amigo-ale/index.html", "/posts/2014/11/20/la-prueba-del-dulce-de-leche-un-cuento-regalo-de-cumpleanos-para-mi-amigo-ale.html"], ["2013/03/16/el-programador-poesia/index.html", "/posts/2013/03/16/el-programador-poesia.html"], ["2011/10/04/el-pelo-en-el-jabon-en-la-radio/index.html", "/posts/2011/10/04/el-pelo-en-el-jabon-en-la-radio.html"], ["2012/06/09/entrevista/index.html", "/posts/2012/06/09/entrevista.html"], ["2009/12/06/primera-vez-con-ruby/index.html", "/posts/2009/12/06/primera-vez-con-ruby.html"], ["2009/07/25/dulzuras-en-el-cumple-de-mama/index.html", "/posts/2009/07/25/dulzuras-en-el-cumple-de-mama.html"], ["2009/06/12/euler-4-python/index.html", "/posts/2009/06/12/euler-4-python.html"], ["2006/06/05/cartilla-de-python-de-una-pagina/index.html", "/posts/2006/06/05/cartilla-de-python-de-una-pagina.html"], ["2009/01/26/la-historia-de-python-historia-personal-parte-1-cwi/index.html", "/posts/2009/01/26/la-historia-de-python-historia-personal-parte-1-cwi.html"], ["2006/04/25/lingo-en-gnulinux/index.html", "/posts/2006/04/25/lingo-en-gnulinux.html"], ["2010/05/17/la-historia-de-python-y-la-serpiente-ataca/index.html", "/posts/2010/05/17/la-historia-de-python-y-la-serpiente-ataca.html"], ["2011/05/06/charla-entendiendo-decoradores-en-python-actualizada/index.html", "/posts/2011/05/06/charla-entendiendo-decoradores-en-python-actualizada.html"], ["2010/08/07/functools-update_wrapper/index.html", "/posts/2010/08/07/functools-update_wrapper.html"], ["2013/12/26/xolopes-40/index.html", "/posts/2013/12/26/xolopes-40.html"], ["2010/11/12/decorando-decoradores/index.html", "/posts/2010/11/12/decorando-decoradores.html"], ["2006/07/09/luchas/index.html", "/posts/2006/07/09/luchas.html"], ["2007/06/08/los-esperamos-en-santa-fe/index.html", "/posts/2007/06/08/los-esperamos-en-santa-fe.html"], ["2014/09/17/videos-en-la-feria-del-libro-de-santa-fe-2014-1er-domingo/index.html", "/posts/2014/09/17/videos-en-la-feria-del-libro-de-santa-fe-2014-1er-domingo.html"], ["orsai/index.html", "/stories/orsai.html"], ["2014/09/05/mail_safe-0-3-2-released/index.html", "/posts/2014/09/05/mail_safe-0-3-2-released.html"], ["2007/08/14/de-regreso-de-las-7mas-jornadas-regionales-de-software-libre/index.html", "/posts/2007/08/14/de-regreso-de-las-7mas-jornadas-regionales-de-software-libre.html"], ["2007/12/10/pirata/index.html", "/posts/2007/12/10/pirata.html"], ["2010/04/03/huevos-de-pascua-caseros/index.html", "/posts/2010/04/03/huevos-de-pascua-caseros.html"], ["2010/06/09/el-sahara-desde-el-cielo/index.html", "/posts/2010/06/09/el-sahara-desde-el-cielo.html"], ["2007/05/16/los-animales-de-ubuntu/index.html", "/posts/2007/05/16/los-animales-de-ubuntu.html"], ["2007/11/01/lo-siento-pero-no-soy-un-hombre-de-ole-bajo-el-brazo/index.html", "/posts/2007/11/01/lo-siento-pero-no-soy-un-hombre-de-ole-bajo-el-brazo.html"], ["2012/01/30/back-from-vacations/index.html", "/posts/2012/01/30/back-from-vacations.html"], ["2005/11/19/5tas-jornadas-regionales-de-software-libre/index.html", "/posts/2005/11/19/5tas-jornadas-regionales-de-software-libre.html"], ["2009/07/02/euler-8-python/index.html", "/posts/2009/07/02/euler-8-python.html"], ["2010/12/17/egyptian-software/index.html", "/posts/2010/12/17/egyptian-software.html"], ["2009/04/19/pan-lactal/index.html", "/posts/2009/04/19/pan-lactal.html"], ["2008/07/29/buen-viaje-y-nuevo-blog-en-la-familia/index.html", "/posts/2008/07/29/buen-viaje-y-nuevo-blog-en-la-familia.html"], ["2012/05/12/casa-tomada-leido-por-cortazar/index.html", "/posts/2012/05/12/casa-tomada-leido-por-cortazar.html"], ["2012/05/08/los-eternos-cuento/index.html", "/posts/2012/05/08/los-eternos-cuento.html"], ["2010/01/08/big-refactoring-en-dyntaint-py/index.html", "/posts/2010/01/08/big-refactoring-en-dyntaint-py.html"], ["2009/01/21/la-historia-de-python-filosofia-de-diseno/index.html", "/posts/2009/01/21/la-historia-de-python-filosofia-de-diseno.html"], ["2010/12/21/lo-que-me-llego-de-china/index.html", "/posts/2010/12/21/lo-que-me-llego-de-china.html"], ["2006/07/23/olpc-en-argentina/index.html", "/posts/2006/07/23/olpc-en-argentina.html"], ["2014/08/18/como-un-programador-escribe-una-novela/index.html", "/posts/2014/08/18/como-un-programador-escribe-una-novela.html"], ["2007/12/20/23/index.html", "/posts/2007/12/20/23.html"], ["libros/xolopes/index.html", "/stories/libros/xolopes.html"], ["2008/04/28/algunas-imagenes-de-flisol-2008-en-santa-fe/index.html", "/posts/2008/04/28/algunas-imagenes-de-flisol-2008-en-santa-fe.html"], ["2008/01/11/%c2%bfconocias-axxon/index.html", "/posts/2008/01/11/aconocias-axxon.html"], ["2012/06/25/antologia-de-literatura-fantastica/index.html", "/posts/2012/06/25/antologia-de-literatura-fantastica.html"], ["2012/12/28/librito-souvenir/index.html", "/posts/2012/12/28/librito-souvenir.html"], ["2010/04/27/python-taint-mode-en-owasp-app-sec-estocolmo-2010/index.html", "/posts/2010/04/27/python-taint-mode-en-owasp-app-sec-estocolmo-2010.html"], ["2007/01/16/la-orden-del-fenix/index.html", "/posts/2007/01/16/la-orden-del-fenix.html"], ["2007/10/23/te-compro-criptonomicon-1-el-codigo-enigma/index.html", "/posts/2007/10/23/te-compro-criptonomicon-1-el-codigo-enigma.html"], ["2009/03/27/fpdf-en-django/index.html", "/posts/2009/03/27/fpdf-en-django.html"], ["2012/02/15/el-cuento-excluido/index.html", "/posts/2012/02/15/el-cuento-excluido.html"], ["2014/09/17/como-un-programador-escribe-una-novela-video/index.html", "/posts/2014/09/17/como-un-programador-escribe-una-novela-video.html"], ["2012/09/15/historia-del-guerrero-y-la-cautiva/index.html", "/posts/2012/09/15/historia-del-guerrero-y-la-cautiva.html"], ["2009/11/01/fierita-sobre-ubuntu/index.html", "/posts/2009/11/01/fierita-sobre-ubuntu.html"], ["2006/02/10/actualizando-a-wp-201/index.html", "/posts/2006/02/10/actualizando-a-wp-201.html"], ["2014/09/22/tomates-plasticos/index.html", "/posts/2014/09/22/tomates-plasticos.html"], ["2006/05/24/count/index.html", "/posts/2006/05/24/count.html"], ["2015/01/01/lei-5-libros-cortitos-antes-de-que-se-termine-el-ano/index.html", "/posts/2015/01/01/lei-5-libros-cortitos-antes-de-que-se-termine-el-ano.html"], ["2006/06/08/no-me-molestes/index.html", "/posts/2006/06/08/no-me-molestes.html"], ["2005/11/04/the-art-of-unix-programming/index.html", "/posts/2005/11/04/the-art-of-unix-programming.html"], ["2006/12/26/nuevamente-en-linea/index.html", "/posts/2006/12/26/nuevamente-en-linea.html"], ["2008/10/14/voy-a-empezar-a-revisionar-mini-lisp/index.html", "/posts/2008/10/14/voy-a-empezar-a-revisionar-mini-lisp.html"], ["2007/04/09/felices-pascuas/index.html", "/posts/2007/04/09/felices-pascuas.html"]]

# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.
DEPLOY_COMMANDS = {
    'default': [
        "rsync -rav --delete output/ jjconti2@juanjoconti.com:juanjoconti.com",
    ]
}

# For user.github.io OR organization.github.io pages, the DEPLOY branch
# MUST be 'master', and 'gh-pages' for other repositories.
# GITHUB_SOURCE_BRANCH = 'master'
# GITHUB_DEPLOY_BRANCH = 'gh-pages'

# The name of the remote where you wish to push to, using github_deploy.
# GITHUB_REMOTE_NAME = 'origin'

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, only .php files uses filters to inject PHP into
# Nikola’s templates. All other filters must be enabled through FILTERS.
#
# Many filters are shipped with Nikola. A list is available in the manual:
# <https://getnikola.com/handbook.html#post-processing-filters>
#
# from nikola import filters
# FILTERS = {
#    ".html": [filters.typogrify],
#    ".js": [filters.closure_compiler],
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.atom', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# Compiler to process LESS files.
# LESS_COMPILER = 'lessc'

# A list of options to pass to the LESS compiler.
# Final command is: LESS_COMPILER LESS_OPTIONS file.less
# LESS_OPTIONS = []

# Compiler to process Sass files.
# SASS_COMPILER = 'sass'

# A list of options to pass to the Sass compiler.
# Final command is: SASS_COMPILER SASS_OPTIONS file.s(a|c)ss
# SASS_OPTIONS = []

# #############################################################################
# Image Gallery Options
# #############################################################################

# One or more folders containing galleries. The format is a dictionary of
# {"source": "relative_destination"}, where galleries are looked for in
# "source/" and the results will be located in
# "OUTPUT_PATH/relative_destination/gallery_name"
# Default is:
GALLERY_FOLDERS = {"galleries": "fotos"}
# More gallery options:
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True
#
# Folders containing images to be used in normal posts or pages. Images will be
# scaled down according to IMAGE_THUMBNAIL_SIZE and MAX_IMAGE_SIZE options, but
# will have to be referenced manually to be visible on the site
# (the thumbnail has ``.thumbnail`` added before the file extension).
# The format is a dictionary of {source: relative destination}.

IMAGE_FOLDERS = {'images/posts/nikola': 'posts',
                 'images/posts/wordpress': 'posts',
                 'images/posts/twitpic': 'posts',
                 'images/posts/nokia': 'posts'
}
#IMAGE_FOLDERS = {'images': ''}
IMAGE_THUMBNAIL_SIZE = 580

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to ' old posts, page %d' or ' page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
#
# (translatable) If the following is empty, defaults to BLOG_TITLE:
# INDEXES_TITLE = ""
#
# (translatable) If the following is empty, defaults to ' [old posts,] page %d' (see above):
# INDEXES_PAGES = ""
#
# If the following is True, INDEXES_PAGES is also displayed on the main (the
# newest) index page (index.html):
# INDEXES_PAGES_MAIN = False
#
# If the following is True, index-1.html has the oldest posts, index-2.html the
# second-oldest posts, etc., and index.html has the newest posts. This ensures
# that all posts on index-x.html will forever stay on that page, now matter how
# many new posts are added.
# If False, index-1.html has the second-newest posts, index-2.html the third-newest,
# and index-n.html the oldest posts. When this is active, old posts can be moved
# to other index pages when new posts are added.
# INDEXES_STATIC = True
#
# (translatable) If PRETTY_URLS is set to True, this setting will be used to create
# prettier URLs for index pages, such as page/2/index.html instead of index-2.html.
# Valid values for this settings are:
#   * False,
#   * a list or tuple, specifying the path to be generated,
#   * a dictionary mapping languages to lists or tuples.
# Every list or tuple must consist of strings which are used to combine the path;
# for example:
#     ['page', '{number}', '{index_file}']
# The replacements
#     {number}     --> (logical) page number;
#     {old_number} --> the page number inserted into index-n.html before (zero for
#                      the main page);
#     {index_file} --> value of option INDEX_FILE
# are made.
# Note that in case INDEXES_PAGES_MAIN is set to True, a redirection will be created
# for the full URL with the page number of the main page to the normal (shorter) main
# page URL.
# INDEXES_PRETTY_PAGE_URL = False

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored.
# Can be any of:
# algol
# algol_nu
# arduino
# autumn
# borland
# bw
# colorful
# default
# emacs
# friendly
# fruity
# igor
# lovelace
# manni
# monokai
# murphy
# native
# paraiso_dark
# paraiso_light
# pastie
# perldoc
# rrt
# tango
# trac
# vim
# vs
# xcode
# This list MAY be incomplete since pygments adds styles every now and then.
# CODE_COLOR_SCHEME = 'default'

# If you use 'site-reveal' theme you can select several subthemes
# THEME_REVEAL_CONFIG_SUBTHEME = 'sky'
# You can also use: beige/serif/simple/night/default

# Again, if you use 'site-reveal' theme you can select several transitions
# between the slides
# THEME_REVEAL_CONFIG_TRANSITION = 'cube'
# You can also use: page/concave/linear/none/default

# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = (
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# )

# Show teasers (instead of full posts) in indexes? Defaults to False.
# INDEX_TEASERS = False

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the RSS_FEED, if RSS_TEASERS is True (translatable)
RSS_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

# Append a URL query to the RSS_READ_MORE_LINK in Atom and RSS feeds. Advanced
# option used for traffic source tracking.
# Minimum example for use with Piwik: "pk_campaign=feed"
# The following tags exist and are replaced for you:
# {feedRelUri}                  A relative link to the feed.
# {feedFormat}                  The name of the syndication format.
# Example using replacement for use with Google Analytics:
# "utm_source={feedRelUri}&utm_medium=nikola_feed&utm_campaign={feedFormat}_feed"
RSS_LINKS_APPEND_QUERY = False

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = ""
# I recommend using the Creative Commons' wizard:
# https://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = '&copy; 2005-{date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="https://getnikola.com" rel="nofollow">Nikola</a> - Theme by <a href="http://elblogdehumitos.com.ar/">Manuel Kaufmann</a>         {license}'

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# To use comments, you can choose between different third party comment
# systems.  The following comment systems are supported by Nikola:
#   disqus, facebook, googleplus, intensedebate, isso, livefyre, muut
# You can leave this option blank to disable comments.
COMMENT_SYSTEM = "disqus"
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = "juanjoconti"

# Enable annotations using annotateit.org?
# If set to False, you can still enable them for individual posts and pages
# setting the "annotations" metadata.
# If set to True, you can disable them for individual posts and pages using
# the "noannotations" metadata.
# ANNOTATIONS = False

# Create index.html for page (story) folders?
# WARNING: if a page would conflict with the index file (usually
#          caused by setting slug to `index`), the STORY_INDEX
#          will not be generated for that directory.
# STORY_INDEX = False
# Enable comments on story pages?
# COMMENTS_IN_STORIES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
STRIP_INDEXES = True

# Should the sitemap list directories which only include other directories
# and no files.
# Default to True
# If this is False
# e.g. /2012 includes only /01, /02, /03, /04, ...: don't add it to the sitemap
# if /2012 includes any files (including index.html)... add it to the sitemap
# SITEMAP_INCLUDE_FILELESS_DIRS = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
# ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in <slug>/index.html.
# No web server configuration is required. Also enables STRIP_INDEXES.
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata.
PRETTY_URLS = True

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you are using the compile-ipynb plugin, just add this one:
# MATHJAX_CONFIG = """
# <script type="text/x-mathjax-config">
# MathJax.Hub.Config({
#     tex2jax: {
#         inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#         displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
#         processEscapes: true
#     },
#     displayAlign: 'left', // Change this to 'center' to center equations.
#     "HTML-CSS": {
#         styles: {'.MathJax_Display': {"margin": 0}}
#     }
# });
# </script>
# """

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# The default is ['fenced_code', 'codehilite']
MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite', 'extra']

# Extra options to pass to the pandoc comand.
# by default, it's empty, is a list of strings, for example
# ['-F', 'pandoc-citeproc', '--bibliography=/Users/foo/references.bib']
# PANDOC_OPTIONS = []

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty (which is
# the default right now)
# (translatable)
# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """

# Show link to source for the posts?
# Formerly known as HIDE_SOURCELINK (inverse)
# SHOW_SOURCELINK = True
# Copy the source files for your pages?
# Setting it to False implies SHOW_SOURCELINK = False
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# By default, Nikola generates RSS files for the website and for tags, and
# links to it.  Set this to False to disable everything RSS-related.
# GENERATE_RSS = True

# By default, Nikola does not generates Atom files for indexes and links to
# them. Generate Atom for tags by setting TAG_PAGES_ARE_INDEXES to True.
# Atom feeds are built based on INDEX_DISPLAY_POST_COUNT and not FEED_LENGTH
# Switch between plain-text summaries and full HTML content using the
# RSS_TEASER option. RSS_LINKS_APPEND_QUERY is also respected. Atom feeds
# are generated even for old indexes and have pagination link relations
# between each other. Old Atom feeds with no changes are marked as archived.
# GENERATE_ATOM = False

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a FeedBurner feed or something else.
# RSS_LINK = None

# Show teasers (instead of full posts) in feeds? Defaults to True.
# RSS_TEASERS = True

# Strip HTML in the RSS feed? Default to False
# RSS_PLAIN = False

# A search form to search this site, for the sidebar. You can use a Google
# custom search (https://www.google.com/cse/)
# Or a DuckDuckGo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# (translatable)
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """
# <!-- DuckDuckGo custom search -->
# <form method="get" id="search" action="//duckduckgo.com/"
#  class="navbar-form pull-left">
# <input type="hidden" name="sites" value="%s">
# <input type="hidden" name="k8" value="#444444">
# <input type="hidden" name="k9" value="#D51920">
# <input type="hidden" name="kt" value="h">
# <input type="text" name="q" maxlength="255"
#  placeholder="Search&hellip;" class="span2" style="margin-top: 4px;">
# <input type="submit" value="DuckDuckGo Search" style="visibility: hidden;">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
#
# If you prefer a Google search form, here's an example that should just work:
# SEARCH_FORM = """
# <!-- Google custom search -->
# <form method="get" action="https://www.google.com/search" class="navbar-form navbar-right" role="search">
# <div class="form-group">
# <input type="text" name="q" class="form-control" placeholder="Search">
# </div>
# <button type="submit" class="btn btn-primary">
# 	<span class="glyphicon glyphicon-search"></span>
# </button>
# <input type="hidden" name="sitesearch" value="%s">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL

# Use content distribution networks for jQuery, twitter-bootstrap css and js,
# and html5shiv (for older versions of Internet Explorer)
# If this is True, jQuery and html5shiv are served from the Google CDN and
# Bootstrap is served from BootstrapCDN (provided by MaxCDN)
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Check for USE_CDN compatibility.
# If you are using custom themes, have configured the CSS properly and are
# receiving warnings about incompatibility but believe they are incorrect, you
# can set this to False.
# USE_CDN_WARNING = True

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
# (translatable)
# EXTRA_HEAD_DATA = ""
# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# (translatable)
# BODY_END = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.md'
# FILE_METADATA_REGEXP = None

# If you hate "Filenames with Capital Letters and Spaces.md", you should
# set this to true.
UNSLUGIFY_TITLES = True

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Open Graph Protocol data for enhancing link sharing and
# discoverability of your site on Facebook, Google+, and other services.
# Open Graph is enabled by default.
# USE_OPEN_GRAPH = True

# Nikola supports Twitter Card summaries, but they are disabled by default.
# They make it possible for you to attach media to Tweets that link
# to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit https://cards-dev.twitter.com/validator
#
# Uncomment and modify to following lines to match your accounts.
# Images displayed come from the `previewimage` meta tag.
# You can specify the card type by using the `card` parameter in TWITTER_CARD.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards
#     # 'card': 'summary',          # Card type, you can also use 'summary_large_image',
#                                   # see https://dev.twitter.com/cards/types
#     # 'site': '@website',         # twitter nick for the website
#     # 'creator': '@username',     # Username for the content creator / author.
# }

# If webassets is installed, bundle JS and CSS into single files to make
# site loading faster in a HTTP/1.1 environment but is not recommended for
# HTTP/2.0 when caching is used. Defaults to True.
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# If you don’t like slugified file names ([a-z0-9] and a literal dash),
# and would prefer to use all the characters your file system allows.
# USE WITH CARE!  This is also not guaranteed to be perfect, and may
# sometimes crash Nikola, your web server, or eat your cat.
# USE_SLUGIFY = True

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []
