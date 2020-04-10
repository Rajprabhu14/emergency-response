from .base import *  # NOQA
# DEBUG = False
ALLOWED_HOSTS = ['localhost']
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

APPEND_SLASH = True
AUTH_USER_MODEL = 'volunteer.Volunteer'
UNREACHABLE_CUSTOMER = 'U'

try:
    from .local_settings import *
except Exception:
    pass
