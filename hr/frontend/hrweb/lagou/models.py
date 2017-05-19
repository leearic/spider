# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Companys_Info(models.Model):
    # lagou 网站招聘信息
    searching_company = models.CharField(max_length=255, verbose_name=u"需要查询的公司名字", default='-')



class Position_URL(models.Model):
    # lagou 网站招聘信息
    searching_company = models.CharField(max_length=255, verbose_name=u"需要查询的公司名字", default='-')
    url = models.CharField(max_length=255, verbose_name=u"查到公司的某个工作岗位的URL", default='-')





class Position_Info(models.Model):
    # lagou 网站招聘信息
    searching_company = models.CharField(max_length=255, verbose_name=u"需要查询的公司名字", default='-')
    searched_company = models.CharField(max_length=255, verbose_name=u"查询到的公司名字", default='-')
    
    bumen = models.CharField(max_length=255, verbose_name=u"部门", default='-')
    zhiwei = models.CharField(max_length=255, verbose_name=u"职位", default='-')
    yaoqiu = models.CharField(max_length=255, verbose_name=u"要求", default='-')
    fabushijian = models.CharField(max_length=255, verbose_name=u"发布时间", default='-')
    
    zhiweiyouhuo = models.CharField(max_length=255, verbose_name=u"职位诱惑", default='-')
    zhiweimiaoshu = models.CharField(max_length=255, verbose_name=u"职位描述", default='-')
    gongzuodidian = models.CharField(max_length=255, verbose_name=u"工作地点", default='-')
    fabuzhe = models.CharField(max_length=255, verbose_name=u"发布者", default='-')