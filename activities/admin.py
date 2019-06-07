# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ActivityCategory, ActivitySheet

# Register your models here.


admin.site.register(ActivitySheet)
admin.site.register(ActivityCategory)