from .base import *

import dj_database_url
import environ

env = environ.Env()
environ.Env.read_env(BASE_DIR / 'env/.env.local')


SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL'),
        conn_max_age=env.int('CONN_MAX_AGE', default=600),
    )
}
