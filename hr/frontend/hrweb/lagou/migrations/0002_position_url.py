# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lagou', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position_URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searching_company', models.CharField(default='-', max_length=255, verbose_name='\u9700\u8981\u67e5\u8be2\u7684\u516c\u53f8\u540d\u5b57')),
                ('url', models.CharField(default='-', max_length=255, verbose_name='\u67e5\u5230\u516c\u53f8\u7684\u67d0\u4e2a\u5de5\u4f5c\u5c97\u4f4d\u7684URL')),
            ],
        ),
    ]
