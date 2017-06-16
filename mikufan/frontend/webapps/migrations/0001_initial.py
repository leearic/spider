# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ad', models.CharField(max_length=255, verbose_name='\u5e7f\u544a\u5185\u5bb9')),
                ('isshow', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Coser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default='NUll', max_length=255, verbose_name='\u6807\u9898')),
                ('content', models.TextField(default='NUll', max_length=255, verbose_name='\u6b63\u6587')),
                ('istop', models.BooleanField(default=False)),
                ('comefrom', models.CharField(default='Mikufan', max_length=255, verbose_name='\u6765\u6e90\u7f51\u7ad9')),
                ('topimage', models.CharField(default='null', max_length=255, verbose_name='\u5c01\u9762\u56fe\u7247')),
                ('addtime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coser_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default='\u6e38\u620f', max_length=255, verbose_name='\u5206\u7c7b')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relate_url', models.CharField(default='NUll', max_length=255, verbose_name='\u56fe\u7247\u5730\u5740')),
                ('real_url', models.CharField(default='NUll', max_length=255, verbose_name='\u771f\u5b9e\u56fe\u7247\u5730\u5740')),
                ('coser', models.ForeignKey(related_name='Coser_Photo', to='webapps.Coser')),
            ],
        ),
        migrations.AddField(
            model_name='coser',
            name='category',
            field=models.ForeignKey(related_name='Coser_Category', to='webapps.Coser_Category'),
        ),
    ]
