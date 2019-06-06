# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SlideImage, HomeTitle, AboutUs, HomeBlurb, FacebookLink, EmailLink

# Register your models here.

admin.site.register(HomeTitle)
admin.site.register(SlideImage)
admin.site.register(HomeBlurb)
admin.site.register(AboutUs)

admin.site.register(FacebookLink)
admin.site.register(EmailLink)


