# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-01 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundraising', '0004_auto_20190301_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='donation',
            field=models.DecimalField(decimal_places=3, default=1.5, max_digits=8),
        ),
    ]