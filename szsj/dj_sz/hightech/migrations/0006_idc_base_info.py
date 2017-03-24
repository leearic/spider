# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hightech', '0005_auto_20170227_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDC_Base_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.IntegerField(max_length=255, verbose_name='\u722c\u53d6\u7f51\u5740')),
                ('name', models.IntegerField(max_length=255, verbose_name='IDC\u540d\u5b57')),
                ('company', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u540d\u5b57')),
                ('zone', models.CharField(max_length=255, verbose_name='\u5730\u533a')),
                ('address', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u5730\u5740')),
                ('phone_number', models.CharField(max_length=255, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('website', models.CharField(max_length=255, verbose_name='\u7f51\u5740')),
                ('Main_business', models.CharField(max_length=255, verbose_name='\u4e3b\u8425\u4e1a\u52a1')),
                ('Satisfaction', models.CharField(max_length=255, verbose_name='\u6ee1\u610f\u5ea6')),
            ],
        ),
    ]