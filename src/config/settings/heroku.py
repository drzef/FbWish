"""
Django settings for heroku  environment
"""
import dj_database_url

from .base import *


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
DATABASES = {'default': dj_database_url.config()}
ALLOWED_HOSTS = ['demo-fbwish.herokuapp.com']

