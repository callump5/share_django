# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.timezone import now

import os


# Create your models here.


# Upload image to Amazon

def upload_staff_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)

    return 'staff/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


# Staff Role

class StaffRole(models.Model):
    role = models.CharField(max_length=200)
    ordering = models.IntegerField()

    def __unicode__(self):
        return str(self.ordering) + ': ' + self.role

    class Meta():
        verbose_name = 'Staff Role'
        verbose_name_plural = 'Staff Roles'


# Staff Details

class StaffDetails(models.Model):
    user = models.ForeignKey(User, related_name='staff_profile')

    bio = HTMLField()

    role = models.ForeignKey(StaffRole, related_name='staff_role')

    staff_image = models.ImageField(upload_to='images/staff')

    def __unicode__(self):
        return self.user.username

    class Meta():
        verbose_name = 'Staff bio'
        verbose_name_plural = 'Staff Details'

