# -*- coding: utf-8 -*-
# Create your models here.
from django.db import models


class CarinfoModel(models.Model):
    u""" 汽车信息，主要是这类汽车的相关信息 """

    # 商品名称
    name = models.CharField(max_length=255, verbose_name=u"商品名称")
    # 购买网址
    url = models.CharField(max_length=255, verbose_name=u"购买网址")
    # 车主
    owner = models.CharField(max_length=255, verbose_name=u"车主")
    # # 车主职业
    # occupation = models.CharField(max_length=255, verbose_name=u"车主职业")
    # # 车主地址
    # owner_address = models.CharField(max_length=255, verbose_name=u"车主地址")
    # # 换车理由
    # reason = models.CharField(max_length=255, verbose_name=u"换车理由")
    # 汽车型号
    module = models.CharField(max_length=255, verbose_name=u"汽车型号")
    # 汽车价格
    price = models.CharField(max_length=255, verbose_name=u"汽车价格")
    # 汽车上牌时间
    registed_time = models.CharField(max_length=255, verbose_name=u"汽车上牌时间")
    # 行程
    mileage = models.CharField(max_length=255, verbose_name=u"行程")
    # 排量
    displacement = models.CharField(max_length=255, verbose_name=u"排量")
    # 汽车所在地
    car_address = models.CharField(max_length=255, verbose_name=u"汽车所在地")
    # 车主说明
    owner_say = models.CharField(max_length=255, verbose_name=u"车主说明")
    image = models.CharField(max_length=255, verbose_name=u"汽车展示图片0")

    class Meta:
        verbose_name = u'汽车基本信息'
        verbose_name_plural = u'汽车基本信息'



class TestingInfoModel(models.Model):
    u""" 汽车检测信息 """
    car = models.ForeignKey(CarinfoModel, related_name=u"car_testing")
    # 车身颜色
    color = models.CharField(max_length=255, verbose_name=u"车身颜色")
    # 年检时间
    annual_time = models.CharField(max_length=255, verbose_name=u"年检时间")
    # 交强险时间
    delivery_time = models.CharField(max_length=255, verbose_name=u"交强险时间")
    # 商业保险到期时间
    insurance_time = models.CharField(max_length=255, verbose_name=u"商业保险到期时间")
    # 归属地
    address = models.CharField(max_length=255, verbose_name=u"归属地")
    # 过户次数
    transfer_number = models.CharField(max_length=255, verbose_name=u"过户次数")
    # 购车发票
    invoice = models.CharField(max_length=255, verbose_name=u"购车发票")
    # 4s 保养
    maintenance = models.CharField(max_length=255, verbose_name=u"4s保养")
    # 事故排查
    accident_investigation = models.CharField(max_length=255, verbose_name=u"事故排查")
    # 安全检测
    safety_detection = models.CharField(max_length=255, verbose_name=u"安全检测")
    # 外观检测
    appearance_detection = models.CharField(max_length=255, verbose_name=u"外观检测")
    # 驾驶检测
    driving_test = models.CharField(max_length=255, verbose_name=u"驾驶检测")
    # 检测结果
    # result = models.CharField(max_length=255, verbose_name=u"检测结果")

    class Meta:
        verbose_name = u'汽车检测信息'
        verbose_name_plural = u'汽车检测信息'

    
class ImageInfoModel(models.Model):
    u""" 汽车展示图片,网络图片"""
    car = models.ForeignKey(CarinfoModel, related_name=u"car_images")
    url0 = models.CharField(max_length=255, verbose_name=u"汽车展示图片0")
    url1 = models.CharField(max_length=255, verbose_name=u"汽车展示图片1")
    url2 = models.CharField(max_length=255, verbose_name=u"汽车展示图片2")
    url3 = models.CharField(max_length=255, verbose_name=u"汽车展示图片3")
    url4 = models.CharField(max_length=255, verbose_name=u"汽车展示图片4")
    url5 = models.CharField(max_length=255, verbose_name=u"汽车展示图片5")
    url6 = models.CharField(max_length=255, verbose_name=u"汽车展示图片6")
    url7 = models.CharField(max_length=255, verbose_name=u"汽车展示图片7")

class ImageInfoHiddenModel(models.Model):
    u""" 汽车展示图片,本地图片"""
    car = models.ForeignKey(CarinfoModel, related_name=u"car_hidden_images")
    url0 = models.CharField(max_length=255, verbose_name=u"汽车展示图片0")
    url1 = models.CharField(max_length=255, verbose_name=u"汽车展示图片1")
    url2 = models.CharField(max_length=255, verbose_name=u"汽车展示图片2")
    url3 = models.CharField(max_length=255, verbose_name=u"汽车展示图片3")
    url4 = models.CharField(max_length=255, verbose_name=u"汽车展示图片4")
    url5 = models.CharField(max_length=255, verbose_name=u"汽车展示图片5")
    url6 = models.CharField(max_length=255, verbose_name=u"汽车展示图片6")
    url7 = models.CharField(max_length=255, verbose_name=u"汽车展示图片7")

