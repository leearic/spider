# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class anjuke(models.Model):
    zone =   models.CharField(max_length=255, verbose_name=u"所在区域")
    # 网址
    url = models.CharField(max_length=255, verbose_name=u"网站地址")
    # 商品图片
    image =  models.CharField(max_length=255, verbose_name=u"图片地址")
    # 售价
    saleprice =  models.CharField(max_length=255, verbose_name=u"售价")
    # 首付
    shoufu =  models.CharField(max_length=255, verbose_name=u"首付")
    # 月供 *
    monthpay =  models.CharField(max_length=255, verbose_name=u"月付")
    # 单价
    unit_price =  models.CharField(max_length=255, verbose_name=u"单价 /m2")
    # 所在小区 *
    quarters =  models.CharField(max_length=255, verbose_name=u"所在小区")
    # 位置 *
    position =  models.CharField(max_length=255, verbose_name=u"位置")
    # 房型
    apartment =  models.CharField(max_length=255, verbose_name=u"户型")
    # 面积
    area =  models.CharField(max_length=255, verbose_name=u"面积")
    # 朝向
    orientation =  models.CharField(max_length=255, verbose_name=u"朝向")
    # 楼层
    floor =  models.CharField(max_length=255, verbose_name=u"楼层")
    # 装修
    renovation =  models.CharField(max_length=255, verbose_name=u"装修")
    # 类型 *
    type =  models.CharField(max_length=255, verbose_name=u"类型")
    # 商品详细情况
    detail =  models.CharField(max_length=255, verbose_name=u"详细说明")