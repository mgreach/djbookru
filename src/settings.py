import os, sys

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

sys.path.insert(0, rel('..', 'lib'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': rel('database.sqlite'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = rel('static')

MEDIA_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = '$g^_w#9*(an#-gn@l-em@)upegpzqg-u9!!ukhn%c8tuz5=#)u'

if DEBUG:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )    
else:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    'context_processors.custom'
)

AUTHENTICATION_BACKENDS = (
    'accounts.backends.CustomUserBackend',
    'accounts.backends.OpenIdBackend',
    'accounts.backends.TwitterBackend',
    'accounts.backends.FacebookBackend',    
    #'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',    
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'openid_consumer.middleware.OpenIDMiddleware',
    'pagination.middleware.PaginationMiddleware', 
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    rel('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.flatpages',
    'sorl.thumbnail',
    'pagination',
    'socialauth',
    'openid_consumer',
    'dinette',
    'accounts',
    'main',
    'news',
    'comments',
    'claims'
)

DATETIME_FORMAT = 'j N Y, G:i'

#authentication settings
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/auth/login/'

OPENID_REDIRECT_NEXT = '/socialauth/openid/done/'

OPENID_SREG = {"required": "nickname, email", "optional":"postcode, country", "policy_url": ""}
OPENID_AX = [{"type_uri": "http://axschema.org/contact/email", "count": 1, "required": True, "alias": "email"},
             {"type_uri": "fullname", "count": 1 , "required": False, "alias": "fullname"}]

TWITTER_CONSUMER_KEY = 'kxqAh00azOKuxh5ANVvOw'
TWITTER_CONSUMER_SECRET = 'r9qtVVwjtHBSYIM875CTcoSVft7xVHL600x3G8co'
#for testing and add django.local.ru to hosts
#TWITTER_CONSUMER_KEY = 'wOpKCQS3inKOLEL5tVg'
#TWITTER_CONSUMER_SECRET = 'e9c22D4NrMQBfYfE35tDQtHgeZoA0nEDhAuhSfy8tUI'

#forum settings
TOPIC_PAGE_SIZE = 10
REPLY_PAGE_SIZE = 20
FLOOD_TIME = 5
TEMPLATE_CONTEXT_PROCESSORS += (
    "dinette.context_processors.get_announcement",
    "dinette.context_processors.get_site_config",
    "dinette.context_processors.get_forumwide_links"
)

MIDDLEWARE_CLASSES += (
     "dinette.middleware.UserActivity",
)
RANKS_NAMES_DATA = ((30, "Member"), (100, "Senior Member"), (300, 'Star'))

#Google settings
GOOGLE_ANALYTICS = """
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-3919032-4");
pageTracker._trackPageview();
} catch(err) {}</script>
"""

#available options
#NEWS_ON_MAIN, NEWS_ON_PAGE, COMMENT_MAX_LENGTH

try:
    from settings_local import *
except ImportError:
    pass