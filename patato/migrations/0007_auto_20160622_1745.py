# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patato', '0006_auto_20160622_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='storage_folder',
            field=models.FilePathField(allow_folders=True, blank=True, null=True, path='C:\\Users\\seanc\\Dev\\Python\\NMM', verbose_name='目录'),
        ),
    ]
