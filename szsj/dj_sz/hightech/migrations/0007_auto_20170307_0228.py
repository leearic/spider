# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hightech', '0006_idc_base_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hightechinfo',
            name='number',
            field=models.IntegerField(verbose_name='\u5e8f\u53f7'),
        ),
        migrations.AlterField(
            model_name='idc_base_info',
            name='name',
            field=models.CharField(max_length=255, verbose_name='IDC\u540d\u5b57'),
        ),
        migrations.AlterField(
            model_name='idc_base_info',
            name='url',
            field=models.CharField(max_length=255, verbose_name='\u722c\u53d6\u7f51\u5740'),
        ),
    ]
