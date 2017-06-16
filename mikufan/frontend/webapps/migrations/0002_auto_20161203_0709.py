# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coser',
            old_name='comefrom',
            new_name='come_from',
        ),
    ]
