# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-20 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filing', '0023_auto_20170920_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host_net',
            name='ip_info',
            field=models.TextField(blank=True, null=True, verbose_name='ip信息'),
        ),
    ]
