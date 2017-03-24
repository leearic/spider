# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class QiuShi(models.Model):
    user_image = models.CharField(max_length=255, verbose_name=u"用户头像")
    user_name = models.CharField(max_length=255, verbose_name=u"用户昵称")
    content = models.CharField(max_length=255, verbose_name=u"文字内容")
    thumb = models.CharField(max_length=255, verbose_name=u"图片内容")
    video_image = models.CharField(blank=True, max_length=255, verbose_name=u"视频图片")
    video = models.CharField(blank=True, max_length=255, verbose_name=u"视频内容")
    laugh = models.IntegerField(verbose_name=u"笑脸数量")
    coments = models.IntegerField(verbose_name=u"评论数量")
    played = models.IntegerField(verbose_name=u"视频播放量")

#    def __unicode__(self):
#        return u'%s %s '(self.user_name, self.content)