"""
Django settings for test environmenti
"""
import dj_database_url

from .base import *


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
DATABASES = {'default': dj_database_url.config()}

