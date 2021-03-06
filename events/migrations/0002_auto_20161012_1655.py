# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('hours', models.DurationField()),
                ('location', models.CharField(max_length=255)),
                ('menu_up', models.FileField(blank=True, null=True, upload_to='../../../uploads/')),
                ('menu', models.FilePathField(path='../../../uploads/')),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.AlterField(
            model_name='event',
            name='capacity',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
