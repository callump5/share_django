# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-22 15:05
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190305_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hometitle',
            name='title',
        ),
        migrations.AddField(
            model_name='hometitle',
            name='content',
            field=tinymce.models.HTMLField(default='Share'),
            preserve_default=False,
        ),
    ]
