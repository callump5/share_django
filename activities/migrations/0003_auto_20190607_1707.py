# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-07 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20190607_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitysheet',
            old_name='desciption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='activitysheet',
            name='once_date',
            field=models.DateTimeField(blank=True, help_text='not-required', null=True, verbose_name='One Off Date'),
        ),
        migrations.AlterField(
            model_name='activitysheet',
            name='start_date',
            field=models.DateTimeField(blank=True, help_text='not-required', null=True, verbose_name='Re-occuring Start date'),
        ),
    ]
