#!/usr/bin/env python
#coding:utf-8
"""
  Author:  'Aric'
  Purpose: ''
  Created: '2015/7/13'
"""

from django.conf.urls import  url

from . import views

urlpatterns = [
    url(r'^', views.interface, name="insterface"),
]
