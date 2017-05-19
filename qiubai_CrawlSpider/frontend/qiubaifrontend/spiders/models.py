# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class QiuShi(models.Model):
    page_url    = models.CharField(max_length=255, verbose_name=u"网站地址")
    user        = models.CharField(max_length=255, verbose_name=u"用户昵称")
    contents     = models.CharField(max_length=255, verbose_name=u"文字内容")
    type        = models.CharField(max_length=255, verbose_name=u"类型")
    url         = models.CharField(blank=True, max_length=255, verbose_name=u"图片内容")
    url0        = models.CharField(blank=True, default=None, max_length=255, verbose_name=u"视频内容")
    smiling     = models.IntegerField(verbose_name=u"笑脸数量")
    comment_count = models.IntegerField(verbose_name=u"评论数量")


class User(models.Model):
    name            = models.CharField(max_length=255, verbose_name=u"用户昵称")
    fans            = models.IntegerField(verbose_name=u"粉丝数量")
    follow          = models.IntegerField(verbose_name=u"关注数量")
    comment         = models.IntegerField(verbose_name=u"评论数量")

    marriage        = models.CharField(max_length=255, verbose_name=u"婚姻状态")
    occupation      = models.CharField(max_length=255, verbose_name=u"职业")
    constellation   = models.CharField(max_length=255, verbose_name=u"星座")
    age             = models.CharField(max_length=255, verbose_name=u"糗龄")


class Comment(models.Model):
    user        = models.CharField(max_length=255, verbose_name=u"用户昵称")
    qiushiURL   = models.CharField(max_length=255, verbose_name=u"糗事URL")
    comment     = models.CharField(max_length=255, verbose_name=u"评论内容")