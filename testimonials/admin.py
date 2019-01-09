# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Testimonial, Status
# Register your models here.

admin.site.register(Testimonial)
admin.site.register(Status)