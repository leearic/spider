# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companys_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searching_company', models.CharField(default='-', max_length=255, verbose_name='\u9700\u8981\u67e5\u8be2\u7684\u516c\u53f8\u540d\u5b57')),
            ],
        ),
        migrations.CreateModel(
            name='Position_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searching_company', models.CharField(default='-', max_length=255, verbose_name='\u9700\u8981\u67e5\u8be2\u7684\u516c\u53f8\u540d\u5b57')),
                ('searched_company', models.CharField(default='-', max_length=255, verbose_name='\u67e5\u8be2\u5230\u7684\u516c\u53f8\u540d\u5b57')),
                ('bumen', models.CharField(default='-', max_length=255, verbose_name='\u90e8\u95e8')),
                ('zhiwei', models.CharField(default='-', max_length=255, verbose_name='\u804c\u4f4d')),
                ('yaoqiu', models.CharField(default='-', max_length=255, verbose_name='\u8981\u6c42')),
                ('fabushijian', models.CharField(default='-', max_length=255, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('zhiweiyouhuo', models.CharField(default='-', max_length=255, verbose_name='\u804c\u4f4d\u8bf1\u60d1')),
                ('zhiweimiaoshu', models.CharField(default='-', max_length=255, verbose_name='\u804c\u4f4d\u63cf\u8ff0')),
                ('gongzuodidian', models.CharField(default='-', max_length=255, verbose_name='\u5de5\u4f5c\u5730\u70b9')),
                ('fabuzhe', models.CharField(default='-', max_length=255, verbose_name='\u53d1\u5e03\u8005')),
            ],
        ),
    ]
