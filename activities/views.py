# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import SlideImage, EmailLink, FacebookLink
from .models import ActivitySchedule
# Create your views here.

def get_activities(request):

    slides = SlideImage.objects.all()
    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    activities = ActivitySchedule.objects.all().order_by('date')


    args = {

        'slides': slides,
        'facebook': facebook,
        'email': email,

        'activities': activities,
    }

    return render(request, 'activities/activities.html', args)