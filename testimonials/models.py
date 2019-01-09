# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from tinymce.models import HTMLField

# Create your models here.

class Status(models.Model):

    status = models.CharField(max_length=200)

    def __unicode__(self):
        return self.status

    class Meta():
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

class Testimonial(models.Model):

    # TODO: Add function to count and allow up to 5 testimonials active at once

    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200, default='Anonymous')
    content = HTMLField(max_length=500)
    status = models.ForeignKey(Status, related_name='review_status')

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

