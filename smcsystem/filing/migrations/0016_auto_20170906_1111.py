# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-06 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filing', '0015_auto_20170906_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='cq_group',
            name='spark',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='spark 版本信息'),
        ),
        migrations.AddField(
            model_name='cq_group',
            name='storm',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='storm 版本信息'),
        ),
    ]
