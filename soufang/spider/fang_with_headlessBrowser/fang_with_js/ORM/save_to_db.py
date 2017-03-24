#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
@version: 0.0.1
@author: Aric Liang
@license: FreeBSDi 
@contact: leearic@126.com
@file: save_to_db.py
@time: 16-5-26 下午12:21
"""


import sys, os

from fang_with_js.settings import path
if path not in sys.path:
    sys.path.append(path)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soufang.settings")
django.setup()
from webapp.models import anjuke

class anjukeORM(object):
    def Save(self, items):
        anjukeitems = anjuke()

        anjukeitems.zone = items["zone"]
        anjukeitems.url = items["url"]
        anjukeitems.image = items["image"]
        anjukeitems.saleprice = items["saleprice"]
        anjukeitems.shoufu = items["shoufu"]
        anjukeitems.monthpay = items["monthpay"]
        anjukeitems.unit_price = items["unit_price"]
        anjukeitems.quarters = items["quarters"]
        anjukeitems.position = items["position"]
        anjukeitems.apartment = items["apartment"]
        anjukeitems.area = items["area"]
        anjukeitems.orientation = items["orientation"]
        anjukeitems.floor = items["floor"]
        anjukeitems.renovation = items["renovation"]
        anjukeitems.type = items["type"]
        anjukeitems.detail = items["details"]

        anjukeitems.save()

        pass