import environ
from .base import *

env = environ.Env()
environ.Env.read_env()

if env('ENVIRONMENT') == 'production':
    from .prod import *
else:
    from .local import *