# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='szmap',
            name='addtime',
            field=models.CharField(default=b'Null', max_length=255, verbose_name='\u6dfb\u52a0\u65f6\u95f4 '),
        ),
    ]
