# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-03 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0002_auto_20190305_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyCateory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Policy Category',
                'verbose_name_plural': 'Policy Categories',
            },
        ),
        migrations.AddField(
            model_name='fileupload',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_file', to='policies.PolicyCateory'),
            preserve_default=False,
        ),
    ]
