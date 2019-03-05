# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import os
from django.utils.timezone import now

def upload_policy_file(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'policy/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )

# Create your models here.

class FileUpload(models.Model):
    title = models.CharField(max_length=200)
    document = models.FileField(upload_to=upload_policy_file)
    desciption = models.TextField()

    class Meta ():
        verbose_name_plural = 'File Uploads'
        verbose_name = 'File'

    def __unicode__(self):
        return self.title
