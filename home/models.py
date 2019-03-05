# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

import os

from tinymce.models import HTMLField

# Create your models here.


# Upload images to Amazon WS

def upload_home_img(instance, filename):

    filename_base, filename_ext = os.path.split(filename)

    return 'home/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )



# Facebook Link

class FacebookLink(models.Model):

    link = models.CharField(max_length=200)

    def __unicode__(self):
        return 'Facebook Link'

    class Meta():
        verbose_name = 'Facebook Link'
        verbose_name_plural = 'Facebook Link'



# Email Link

class EmailLink(models.Model):

    link = models.CharField(max_length=200)

    def __unicode__(self):
        return 'Email Link'

    class Meta():
        verbose_name = 'Email Link'
        verbose_name_plural = 'Email Link'



# Slide Images

class SlideImage(models.Model):

    img = models.ImageField(upload_to=upload_home_img)

    def __unicode__(self):
        return 'Slide Image - ' + str(self.id)

    class Meta():
        verbose_name = 'Slide Image'
        verbose_name_plural = 'Slide Images'



# Home Title

class HomeTitle(models.Model):

    title = models.CharField(max_length=70)

    def __unicode__(self):
        return ('Home Title')

    class Meta():
        verbose_name = 'Title'
        verbose_name_plural = 'Home Title '



# Home Content

class HomeContent(models.Model):

    title = models.CharField(max_length=70)
    content = HTMLField()

    def __unicode__(self):
        return str('Home Article - ' + str(self.id))

    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Home Articles'



# Home Box

class HomeBox(models.Model):

    header = models.CharField(max_length=200)
    content = HTMLField(max_length=260)

    def __unicode__(self):
        return 'Home Box - ' + str(self.id)

    class Meta():
        verbose_name = 'Home Box'
        verbose_name_plural= 'Home Boxes'


# Background Image

class BackgroundImage(models.Model):

    image = models.ImageField(upload_to=upload_home_img)
    active = models.BooleanField()


    def __unicode__(self):
        return 'Background - ' + str(self.id)

    class Meta():
        verbose_name = 'Background'
        verbose_name_plural= 'Background Images'
