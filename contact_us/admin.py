# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ContactRequest, StaffContact
# Register your models here.

admin.site.register(ContactRequest)
admin.site.register(StaffContact)
