# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from home.models import BackgroundImage, FacebookLink, EmailLink
from fundraising.models import FundraisingTarget, Donations
from .models import Cookies, Privacy
import random

# Create your views here.

def cookies(request):
    cookies = Cookies.objects.all()
    privacy = Privacy.objects.all()

    count = BackgroundImage.objects.filter(active=True).count()
    rand = random.randint(1, count)

    background = BackgroundImage.objects.filter(active=True).get(pk=rand)

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    args = {

        'facebook': facebook,
        'email': email,

        'background': background,

        'cookies': cookies,
        'privacy': privacy
    }

    return render(request, 'cookies/cookies.html', args)

