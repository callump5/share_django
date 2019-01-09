# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from tinymce.models import HTMLField
import os

# Create your models here.

def upload_staff_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'staff/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class Role(models.Model):
    job_role = models.CharField(max_length=200)

    def __unicode__(self):
        return self.job_role

    class Meta():
        verbose_name = 'Job Role'
        verbose_name_plural = 'Job Roles'


class Staff_Bio(models.Model):
    user = models.ForeignKey(User, related_name='staff_profile')
    role = models.ForeignKey(Role, related_name='staff_job_role')
    bio = HTMLField()
    staff_image= models.ImageField(upload_to='images/staff')

    def __unicode__(self):
        return self.user.first_name

    class Meta():
        verbose_name = 'Staff Bio'
        verbose_name_plural = 'Staff Profiles'