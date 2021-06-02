import environ, os
from .base import *


env = environ.Env()
environ.Env.read_env()

DEBUG = True
ALLOWED_HOSTS= ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}