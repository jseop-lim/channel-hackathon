from .base import *

import dj_database_url
import environ

env = environ.Env()
environ.Env.read_env(BASE_DIR / 'env/.env.prod')


SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []


DATABASES = {
    'default': dj_database_url.parse(
        env('DATABASE_URL'),
        conn_max_age=env.int('CONN_MAX_AGE', default=600),
    )
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',  # change debug level as appropiate
            'propagate': False,
        },
    },
}
