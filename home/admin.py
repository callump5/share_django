# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SlideImage, HomeTitle, HomeContent, HomeBox, FacebookLink, EmailLink, BackgroundImage

# Register your models here.

admin.site.register(SlideImage)
admin.site.register(HomeTitle)
admin.site.register(HomeContent)
admin.site.register(HomeBox)

admin.site.register(BackgroundImage)

admin.site.register(FacebookLink)
admin.site.register(EmailLink)


