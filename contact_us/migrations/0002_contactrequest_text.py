# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-10 22:40
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='text',
            field=tinymce.models.HTMLField(default='cycivouvou'),
            preserve_default=False,
        ),
    ]
