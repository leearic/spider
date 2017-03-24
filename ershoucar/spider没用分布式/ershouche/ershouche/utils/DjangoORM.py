# -*- coding: utf-8 -*-
__author__ = 'aric'
import sys, os

from ershouche.settings import path
if path not in sys.path:
    sys.path.append(path)

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ershouche.settings")
django.setup()
from webapp.models import CarModel, CarinfoModel, TestingInfoModel, ImageInfoModel, ImageInfoHiddenModel
class CarORM(object):
    def SaveCarInfo(self, item):

        # 售车信息
        carinfomodel = CarinfoModel()
        carinfomodel.owner = item["owner"][0]
        carinfomodel.module = item["module"][0]
        carinfomodel.price = item["price"][0]
        carinfomodel.registed_time = item["registed_time"][0]
        carinfomodel.mileage = item["mileage"][0]
        carinfomodel.displacement = item["displacement"][0]
        carinfomodel.car_address = item["car_address"][0]
        carinfomodel.owner_say = item["owner_say"][0]
        carinfomodel.save()

        # 汽车检测报告
        testinginf = TestingInfoModel()
        testinginf.color = item["color"][0]
        testinginf.annual_time = item["annual_time"][0]
        testinginf.delivery_time = item["delivery_time"][0]
        testinginf.insurance_time = item["insurance_time"][0]
        testinginf.address = item["address"][0]
        testinginf.transfer_number = item["transfer_number"][0]
        testinginf.invoice = item["invoice"][0]
        testinginf.maintenance = item["maintenance"][0]
        testinginf.accident_investigation = item["accident_investigation"][0]
        testinginf.safety_detection = item["safety_detection"][0]
        testinginf.appearance_detection = item["appearance_detection"][0]
        testinginf.driving_test = item["driving_test"][0]
        testinginf.save()

        # 汽车展示图片
        imagemodel = ImageInfoModel()
        imagemodel.url0 = item["url0"][0]
        imagemodel.url1 = item["url1"][0]
        imagemodel.url2 = item["url2"][0]
        imagemodel.url3 = item["url3"][0]
        imagemodel.url4 = item["url4"][0]
        imagemodel.url5 = item["url5"][0]
        imagemodel.url6 = item["url6"][0]
        imagemodel.url6 = item["url7"][0]
        imagemodel.save()

        # 汽车展示图片
        imagehiddenmodel = ImageInfoHiddenModel()
        imagehiddenmodel.url0 = item["url0"][0]
        imagehiddenmodel.url1 = item["url1"][0]
        imagehiddenmodel.url2 = item["url2"][0]
        imagehiddenmodel.url3 = item["url3"][0]
        imagehiddenmodel.url4 = item["url4"][0]
        imagehiddenmodel.url5 = item["url5"][0]
        imagehiddenmodel.url6 = item["url6"][0]
        imagehiddenmodel.url6 = item["url7"][0]
        imagehiddenmodel.save()

                # 汽车主题
        carmodel = CarModel()
        carmodel.name = item["name"][0]
        carmodel.url  = item["url"][0]
        carmodel.info = carinfomodel
        carmodel.test = testinginf
        carmodel.image = imagemodel
        carmodel.hidd_image = imagehiddenmodel
        carmodel.save()
