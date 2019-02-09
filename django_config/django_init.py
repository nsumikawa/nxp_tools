"""
    Configure
    ==============

    Description
    -----------
    Configures the django settings based on the current project to allow for
    remote access of the django API and databases

    author : Nik Sumikawa
    Date : June 13, 2017
"""

import logging

def initialize():
    """
    Configures the django setting to allow for access to the django databases
    and the model API
    """

    from excursion.django_config import settings
    from django.conf import settings as settings_api
    from django.apps import apps

    log = logging.getLogger(__name__)

    log.debug( 'initializing django interface' )
    #retrieve the list of installed apps
    installed_apps = list(settings.INSTALLED_APPS)

    #replace all personally owned apps with their full path
    for app in settings.MY_APPS :
        index = installed_apps.index( app )
        installed_apps[index] = settings.MY_APPS[app]

    conf = {
        'INSTALLED_APPS': tuple( installed_apps),
        'DATABASES' : settings.DATABASES,
        'TIME_ZONE': 'UTC'
    }

    settings_api.configure(**conf)
    apps.populate(settings_api.INSTALLED_APPS)

    return settings.STATIC_PATH
