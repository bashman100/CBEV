# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20161017_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
