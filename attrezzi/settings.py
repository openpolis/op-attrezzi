"""
Settings for Attrezzi are all namespaced in the ATTREZZI setting.

This module provides the `attrezzi_setting` object, that is used to access
Attrezzi settings, checking for user settings first, then falling
back to the defaults.
"""
from __future__ import unicode_literals
from django.conf import settings


USER_SETTINGS = getattr(settings, 'ATTREZZI', None)

DEFAULTS = {
    # Accesso policies
    # 'ACCESSO_ACCESS_TOKEN_URL': 'http://accesso.depp.it/o/token/',
    # 'ACCESSO_AUTHORIZE_URL': 'http://accesso.depp.it/o/authorize/',
    # 'ACCESSO_PROFILE_URL': 'http://accesso.depp.it/api/v1/users/me',
    'ACCESSO_ACCESS_TOKEN_URL': 'http://op.accesso:8111/o/token/',
    'ACCESSO_AUTHORIZE_URL': 'http://op.accesso:8111/o/authorize/',
    'ACCESSO_PROFILE_URL': 'http://op.accesso:8111/api/v1/users/me',

}


class AttrezziSettings(object):
    """
    A settings object, that allows API settings to be accessed as properties.
    For example:

        from rest_framework.settings import api_settings
        print api_settings.DEFAULT_RENDERER_CLASSES

    Any setting with string import paths will be automatically resolved
    and return the class, rather than the string literal.
    """
    def __init__(self, user_settings=None, defaults=None):
        self.user_settings = user_settings or {}
        self.defaults = defaults or {}

    def __getattr__(self, attr):
        if attr not in self.defaults.keys():
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        self.validate_setting(attr, val)

        # Cache the result
        setattr(self, attr, val)
        return val

    def validate_setting(self, attr, val):
        if attr == 'FILTER_BACKEND' and val is not None:
            # Make sure we can initialize the class
            val()

attrezzi_settings = AttrezziSettings(USER_SETTINGS, DEFAULTS)
