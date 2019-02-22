# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Privacy(models.Model):
    info = HTMLField()

    class Meta():
        verbose_name_plural = 'Cookie page info'
        verbose_name = 'Info'
    def __unicode__(self):
        return 'privacy'



class Cookies(models.Model):
    name = models.CharField(max_length=200)
    desription = HTMLField()

    class Meta():
        verbose_name_plural = 'Cookies'
        verbose_name= 'Cookie'

    def __unicode__(self):
        return self.name

