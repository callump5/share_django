# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-06 14:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190606_1443'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeContent',
            new_name='AboutUs',
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'About Info', 'verbose_name_plural': 'About Info'},
        ),
    ]
