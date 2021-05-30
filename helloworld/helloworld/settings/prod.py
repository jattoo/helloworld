from logging import DEBUG
import environ
from .base import *


env = environ.Env()
environ.Env.read_env()


DEBUG=env('DEBUG')
ALLOWED_HOSTS= env('ALLOWED_HOSTS').split(',')
ADMINS = (
    ('moe', 'm_krub@aol.com'),
)



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('PROD_DATABASE_NAME'),
        'USER': env('PROD_DATABASE_USER'),
        'PASSWORD': env('PROD_DATABASE_PASSWORD'),
        'HOST': env('PROD_DATABASE_HOST'),
        'PORT': env('PROD_DATABASE_PORT')
    }
}