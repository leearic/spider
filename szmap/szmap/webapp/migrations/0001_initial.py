# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='szmap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zone', models.CharField(max_length=255, verbose_name='\u533a\u57df\u540d\u79f0 ')),
                ('zhishu', models.CharField(max_length=255, verbose_name='\u4ea4\u901a\u6307\u6570 ')),
                ('chesu', models.CharField(max_length=255, verbose_name='\u5e73\u5747\u8f66\u901f ')),
                ('dengji', models.CharField(max_length=255, verbose_name='\u62e5\u5835\u7b49\u7ea7 ')),
            ],
        ),
    ]
