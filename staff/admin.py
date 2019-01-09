# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Role, Staff_Bio
# Register your models here.

admin.site.register(Role)
admin.site.register(Staff_Bio)
