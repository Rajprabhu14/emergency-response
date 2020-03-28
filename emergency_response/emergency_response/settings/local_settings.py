from .base import *  # noqa
# DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'response',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

GEONAMES_URL = 'http://api.geonames.org/searchJSON'
GEONAME_PARAMS = {
    'country': "IN",
    'maxRows': 5,
    'username': 'rajprabhu_kcube',
    'q': ''
}
MAP_MY_INDIA_URL = 'https://www.mapmyindia.com/api/advanced-maps/doc/sample/getrespgeocode.php'

MAP_MY_INDIA__PARAMS = {
    'address': '',
    'itemCount': 1,
    'bias': 0
}
APPEND_SLASH = True
