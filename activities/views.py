# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import SlideImage, EmailLink, FacebookLink
from .models import ActivitySheet, ActivityCategory

# Create your views here.

def get_activities(request):

    slides = SlideImage.objects.all()
    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    activities = ActivitySheet.objects.all()
    categories = ActivityCategory.objects.all()


    args = {

        'slides': slides,
        'facebook': facebook,
        'email': email,

        'activities': activities,
        'categories': categories
    }

    return render(request, 'activities/activities.html', args)