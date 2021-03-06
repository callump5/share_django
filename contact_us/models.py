# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField

# Create your models here.

class StaffContact(models.Model):

    user = models.ForeignKey(User, related_name='staff_contact')
    number = models.CharField(max_length=15)
    email = models.CharField(max_length=300)

    def __unicode__(self):
        return self.user.get_full_name()

    class Meta():
        verbose_name = 'Staff Contact Info'
        verbose_name_plural = 'Staff Contact Details'


class ContactRequest(models.Model):

    name = models.CharField(max_length=300, null=False)
    number = models.CharField(max_length=300)
    email = models.EmailField()

    text = HTMLField()

    def __unicode__(self):
        return self.name

    class Meta():
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Requests'

class OpenTimes(models.Model):
    day = models.CharField(max_length=300)
    times = models.CharField(max_length=400)

    def __unicode__(self):
        return self.day

    class Meta():
        verbose_name = 'Opening Time'
        verbose_name_plural = 'Opening Times'
