# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.utils.timezone import now

from django.db import models


# Create your models here.


def upload_activity_image(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'activities/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class ActivityCategory(models.Model):
    category = models.CharField(max_length=300)

    class Meta():
        verbose_name_plural = 'Activity Categories'
        verbose_name = 'Activity Category'

    def __unicode__(self):
        return self.category


class ActivitySheet(models.Model):
    category = models.ForeignKey(ActivityCategory, related_name='category_file')
    title = models.CharField(max_length=200)
    document = models.FileField(upload_to=upload_activity_image)
    description = models.TextField()
    slots = models.IntegerField()
    start_date = models.DateTimeField(u'Re-occuring Start date', help_text='not-required', null=True, blank=True)
    once_date = models.DateTimeField(u'One Off Date', help_text='not-required',null=True, blank=True)

    class Meta ():
        verbose_name_plural = 'Activity Sheets'
        verbose_name = 'Activity Sheet'

    def __unicode__(self):
        return self.title
