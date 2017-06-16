# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.


class cosplay8dotcom(models.Model):
    base_html_url = models.CharField(max_length=255, verbose_name=u"网页地址")
    base_image_url = models.CharField(max_length=255, verbose_name=u"图片地址")
    base_image_content = models.CharField(max_length=255, verbose_name=u"标题")