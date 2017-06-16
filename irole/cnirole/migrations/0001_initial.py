# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cosplay8dotcom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_html_url', models.CharField(max_length=255, verbose_name='\u7f51\u9875\u5730\u5740')),
                ('base_image_url', models.CharField(max_length=255, verbose_name='\u56fe\u7247\u5730\u5740')),
                ('base_image_content', models.CharField(max_length=255, verbose_name='\u6807\u9898')),
            ],
        ),
    ]
