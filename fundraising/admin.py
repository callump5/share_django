# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import FundraisingTarget, Donations

# Register your models here.

admin.site.register(FundraisingTarget)
admin.site.register(Donations)
