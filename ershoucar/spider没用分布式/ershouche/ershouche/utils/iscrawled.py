# -*- coding: utf-8 -*-
__author__ = 'aric'
import sys, os

from ershouche.settings import path
if path not in sys.path:
    sys.path.append(path)

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ershoucar.settings")
django.setup()
from webapp.models import CarModel

class iscrawled(object):

    def IsCrawled(self, url):
        try:
            aa = CarModel.objects.filter(url=url)
            if len(aa) != 0:
                return  False
            else:
                return True
        except Exception, e:
            return  True