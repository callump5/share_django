# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class FileUpload(models.Model):
    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents/')
    desciption = models.TextField()

    class Meta ():
        verbose_name_plural = 'File Uploads'
        verbose_name = 'File'

    def __unicode__(self):
        return self.title
