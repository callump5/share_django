# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-17 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_auto_20190305_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsers',
            name='website',
            field=models.CharField(default='weg', max_length=500),
            preserve_default=False,
        ),
    ]