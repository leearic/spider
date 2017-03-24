"""
WSGI config for baixihecom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

path = '/var/www/html/django'
if path not in sys.path:
        sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baixihecom.settings")

application = get_wsgi_application()
