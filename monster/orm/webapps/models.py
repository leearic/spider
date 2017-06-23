# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Day_News(models.Model):
    # 每日新闻地址， 按天算的
    url = models.CharField(max_length=255, verbose_name=u"每日新闻真实URL")
    md5 = models.CharField(max_length=255, verbose_name=u"每日新闻真实URL的MD5")

class Daily_News(models.Model):
    # 每日新闻的真实URL, 每天新闻里的每条新闻
    url = models.CharField(max_length=255, verbose_name=u"每条新闻的真实URL")
    md5 = models.CharField(max_length=255, verbose_name=u"每条新闻真实URL的MD5")

class News_Real_Content(models.Model):
    # 每条新闻的具体内容
    # news         = models.ForeignKey(Daily_News, related_name='Day_News')
    url          = models.CharField(max_length=255, verbose_name=u"网址", default='nil')
    title        = models.CharField(max_length=255, verbose_name=u"新闻标题", default='nil')
    content      = models.TextField(max_length=1999, verbose_name=u"新闻具体内容", default='nil')
    content_time = models.CharField(max_length=255, verbose_name=u"新闻时间", default='nil')
    content_from = models.CharField(max_length=255, verbose_name=u"新闻来源", default='nil')
    content_type = models.CharField(max_length=255, verbose_name=u"新闻类型", default='文字新闻')
    content_web  = models.CharField(max_length=255, verbose_name=u"新闻爬取来源", default='来源')
    save_time    = models.CharField(max_length=255, verbose_name=u"记录爬取时间", default='nil')
    content_html = models.TextField(max_length=1999, default='nil', verbose_name=u"新闻具体内容源码")
