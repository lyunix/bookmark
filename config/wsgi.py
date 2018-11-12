"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
#import sys
#path = '/home/lyun/bookmark'
#if path not in sys.path:
#    sys.path.append(path)

#from django.contriib.staticfiles.handlers import StaticFilesHandler
#from django.core.wsgi import get_wsgi_application

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
