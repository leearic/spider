# -*- coding: utf-8 -*-
from django.contrib import  admin
from qiubai.models import  QiuShi

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'laugh', 'played')
    search_fields = ('user_name', 'content')

admin.site.register(QiuShi, AuthorAdmin)