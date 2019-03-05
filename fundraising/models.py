# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import os
from django.utils.timezone import now

from django.db import models
from tinymce.models import HTMLField

# Create your models here.


def upload_fundraising_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'fundraising/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class FundraisingTarget(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    target = models.DecimalField(decimal_places=2, max_digits=7)
    active = models.BooleanField()

    image_1 = models.ImageField(upload_to=upload_fundraising_img)
    image_2 = models.ImageField(upload_to=upload_fundraising_img, help_text='Not required', null=True, blank=True)
    image_3 = models.ImageField(upload_to=upload_fundraising_img, help_text='Not required', null=True, blank=True)

    def __unicode__(self):
        return self.title

    def count_achieved(self):
        donations = Donations.objects.all().filter(target=self.id)
        acheived = 0
        for donation in donations:
            acheived += donation.donation
        return acheived


    class Meta():
        verbose_name = 'Fundraising Target'
        verbose_name_plural = 'Fundraising Targets'


class Donations(models.Model):

    target = models.ForeignKey(FundraisingTarget)
    donation = models.DecimalField(max_digits=8, decimal_places=2, default=1.50)
    

    stripe_id = models.CharField(max_length=40, default='')

    def __unicode__(self):
        return 'Donation'

    class Meta():
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'


