# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

import django
# Create your models here.
from django.utils.safestring import mark_safe
#



class Coser(models.Model):
    u""" Coser 整片文章  """
    # 分类
    title = models.CharField(max_length=255, verbose_name=u"标题", blank=False, default=u'NUll')
    content  = models.TextField(max_length=255, verbose_name=u"正文", blank=False, default=u'NUll')

    istop    = models.BooleanField(default=False, verbose_name=u"置顶")
    come_from = models.CharField(max_length=255, verbose_name=u"来源网站", default=u"Mikufan")
    topimage = models.CharField(max_length=255, verbose_name=u"封面图片", default=u"null")
    addtime  = models.DateTimeField(default=django.utils.timezone.now, blank=True, verbose_name=u"添加时间")


    def topimage_tag(self):
        result = '<img src="%s", width=200px />' % self.topimage
        return mark_safe(result)

    topimage_tag.allow_tags = True
    topimage_tag.short_description = u"图片预览"



class Category(models.Model):
    u""" 图片分类 比如： 游戏角色 ，漫画角色 """
    # 分类
    coser    = models.ForeignKey(Coser, related_name=u"Coser_Category")
    category = models.CharField(max_length=255, verbose_name=u"分类", default=u'游戏')


class Images(models.Model):
    u""" Coser 图片，一个Coser可能有多个图片 """
    # 分类
    coser      = models.ForeignKey(Coser, related_name=u"Coser_Photo")
    relate_url = models.CharField(max_length=255, verbose_name=u"图片地址", default=u'NUll')
    real_url   = models.CharField(max_length=255, verbose_name=u"真实图片地址", default=u'NUll')



    def relate_url_tag(self):
        result1 = '<img src="%s", width=200px />' % self.relate_url
        return mark_safe(result1)

    def real_url_tag(self):
        result2 = '<img src="%s", width=200px />' % self.real_url
        return mark_safe(result2)

    relate_url_tag.allow_tags = True
    relate_url_tag.short_description = u"相对图片预览"

    real_url_tag.allow_tags = True
    real_url_tag.short_description = u"原始图片预览"





class Ads(models.Model):
    u"""广告相关"""
    ad = models.CharField(max_length=255, verbose_name=u"广告内容")
    isshow = models.BooleanField(default=False)
