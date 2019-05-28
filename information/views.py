# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import HomeTitle, SlideImage, EmailLink, FacebookLink
from information.models import InfoContent, StickyNote, Sponsers

import random

# Create your views here.

def get_info(request):

    title = HomeTitle.objects.get(pk=1)
    slides = SlideImage.objects.all()
    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    info = InfoContent.objects.all()
    notes = StickyNote.objects.all()
    sponser = Sponsers.objects.all()

    args = {
        'title': title,
        'slides': slides,
        'facebook': facebook,
        'email': email,
        'info': info,
        'notes': notes,
        'sponsers': sponser,
    }


    return render(request, 'info/info.html', args)
