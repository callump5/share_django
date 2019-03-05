# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-05 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import fundraising.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation', models.DecimalField(decimal_places=2, default=1.5, max_digits=8)),
                ('stripe_id', models.CharField(default='', max_length=40)),
            ],
            options={
                'verbose_name': 'Donation',
                'verbose_name_plural': 'Donations',
            },
        ),
        migrations.CreateModel(
            name='FundraisingTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', tinymce.models.HTMLField()),
                ('target', models.DecimalField(decimal_places=2, max_digits=7)),
                ('active', models.BooleanField()),
                ('image_1', models.ImageField(upload_to=fundraising.models.upload_fundraising_img)),
                ('image_2', models.ImageField(blank=True, help_text='Not required', null=True, upload_to=fundraising.models.upload_fundraising_img)),
                ('image_3', models.ImageField(blank=True, help_text='Not required', null=True, upload_to=fundraising.models.upload_fundraising_img)),
            ],
            options={
                'verbose_name': 'Fundraising Target',
                'verbose_name_plural': 'Fundraising Targets',
            },
        ),
        migrations.AddField(
            model_name='donations',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fundraising.FundraisingTarget'),
        ),
    ]
