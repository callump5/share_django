# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import ActivitySheet, ActivityCategory

# Create your views here.

def get_activities(request):

    activities = ActivitySheet.objects.all()
    categories = ActivityCategory.objects.all()


    args = {
        'activities': activities,
        'categories': categories
    }

    return render(request, 'activities/activities.html', args)