"""
Excursion Detection wsgi
==============

author : Nik Sumikawa
Date : Dec 7, 2018
"""

import os
import sys
import platform
import logging

import django
from django.core.wsgi import get_wsgi_application

from common.setup.defines import create_folder
from common.utils.operating_system.logger import initialize_logging



#add path for server
if platform.node() == 'az84cqc01':
    sys.path.append('/home/nxa18331/git/nxp_tools')
    sys.path.append('/home/nxa18331/git/nxp_tools/django_config')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_config.settings")

django.setup()

#initialize the logger
if platform.node() == 'az84cqc01':path = '/home/nxa18331/logs/web/nxp_tools'
else : path = '%s/logs' % os.path.dirname(os.path.abspath(__file__))
create_folder( path )
initialize_logging( path=path, level=logging.DEBUG )


application = get_wsgi_application()
