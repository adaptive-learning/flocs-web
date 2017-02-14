""" Django settings for testing
"""
from .. import settings

# Import all actual settings
from ..settings import *

# Add test package to installed apps so that Django finds models defined for
# testing purposes
INSTALLED_APPS = settings.INSTALLED_APPS + [
    'flocsweb.tests',
]
