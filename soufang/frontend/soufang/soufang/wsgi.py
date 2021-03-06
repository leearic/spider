"""
WSGI config for soufang project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soufang.settings")

application = get_wsgi_application()
