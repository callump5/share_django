# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import BackgroundImage, EmailLink, FacebookLink
from information.models import InfoContent, StickyNote, Sponsers

import random

# Create your views here.

def get_info(request):

    count = BackgroundImage.objects.filter(active=True).count()
    rand = random.randint(1, count)
    background = BackgroundImage.objects.filter(active=True).get(pk=rand)

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    info = InfoContent.objects.all()
    notes = StickyNote.objects.all()
    sponser = Sponsers.objects.all()

    args = {
        'facebook': facebook,
        'email': email,
        'background': background,
        'info': info,
        'notes': notes,
        'sponsers': sponser,
    }

    return render(request, 'info/info.html', args)
