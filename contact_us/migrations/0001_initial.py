# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-05 13:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('number', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('text', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name': 'Contact Request',
                'verbose_name_plural': 'Contact Requests',
            },
        ),
        migrations.CreateModel(
            name='StaffContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_contactact', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff Contact Info',
                'verbose_name_plural': 'Staff Contact Details',
            },
        ),
    ]
