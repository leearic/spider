# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class szmap(models.Model):
    zone  = models.CharField(max_length=255, verbose_name=u"区域名称 ")
    zhishu = models.CharField(max_length=255, verbose_name=u"交通指数 ")
    chesu   = models.CharField(max_length=255, verbose_name=u"平均车速 ")
    dengji = models.CharField(max_length=255, verbose_name=u"拥堵等级 ")
    addtime = models.CharField(max_length=255, verbose_name=u"添加时间 ", default='Null')