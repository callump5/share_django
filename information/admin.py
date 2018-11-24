# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import InfoContent, StickyNote, Sponsers

# Register your models here.

admin.site.register(InfoContent)
admin.site.register(StickyNote)
admin.site.register(Sponsers)
