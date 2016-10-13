# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20161013_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='logo',
            field=models.FilePathField(blank=True, null=True, path='../assets/img/logos'),
        ),
        migrations.AddField(
            model_name='location',
            name='logo_up',
            field=models.ImageField(blank=True, null=True, upload_to='../assets/img/logos'),
        ),
        migrations.AlterField(
            model_name='location',
            name='hours',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='menu',
            field=models.FilePathField(blank=True, null=True, path='../../../uploads/'),
        ),
    ]
