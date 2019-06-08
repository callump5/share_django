# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.utils.timezone import now

from django.db import models

from tinymce.models import HTMLField


# Create your models here.


def upload_activity_image(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'activities/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class ActivitySchedule(models.Model):
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    document = models.FileField(help_text='Upload any material for the day',upload_to=upload_activity_image, null=True, blank=True)

    activities = HTMLField()
    required = models.TextField(help_text='For any requirements for the students e.g. lunch, spare clothes',null=True, blank=True)
    transport = models.TextField(help_text='Pick up/Drop off points',null=True, blank=True)
    slots = models.IntegerField(blank=True, null=True)

    class Meta ():
        verbose_name_plural = 'Activity Schedule'
        verbose_name = 'Day Activities'

    def __unicode__(self):
        return str(self.date)
