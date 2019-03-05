# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

from tinymce.models import HTMLField

import os


# Create your models here.


def upload_info_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'info/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class InfoContent(models.Model):

    content = HTMLField()

    def __unicode__(self):
        return 'Info Content'

    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Info Article'


class StickyNote(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    image = models.ImageField(upload_to=upload_info_img, null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Sticky Note'
        verbose_name_plural = 'Sticky Notes'


class Sponsers(models.Model):

    company = models.CharField(max_length=250)

    image = models.ImageField(upload_to=upload_info_img)

    def __unicode__(self):
        return self.company

    class Meta():
        verbose_name = 'Sponser'
        verbose_name_plural = 'Sponsers'


