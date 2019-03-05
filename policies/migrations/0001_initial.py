# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-05 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='documents/')),
                ('desciption', models.TextField()),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'File Uploads',
            },
        ),
    ]
