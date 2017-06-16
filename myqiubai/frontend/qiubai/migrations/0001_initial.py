# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QiuShi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_image', models.CharField(max_length=255, verbose_name='\u7528\u6237\u5934\u50cf')),
                ('user_name', models.CharField(max_length=255, verbose_name='\u7528\u6237\u6635\u79f0')),
                ('content', models.CharField(max_length=255, verbose_name='\u6587\u5b57\u5185\u5bb9')),
                ('thumb', models.CharField(max_length=255, verbose_name='\u56fe\u7247\u5185\u5bb9')),
                ('video', models.CharField(max_length=255, verbose_name='\u89c6\u9891\u5185\u5bb9')),
                ('laugh', models.IntegerField(verbose_name='\u7b11\u8138\u6570\u91cf')),
                ('coments', models.IntegerField(verbose_name='\u8bc4\u8bba\u6570\u91cf')),
                ('played', models.IntegerField(verbose_name='\u89c6\u9891\u64ad\u653e\u91cf')),
            ],
        ),
    ]
