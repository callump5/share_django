# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from home.models import FacebookLink, EmailLink
from .models import Cookies, Privacy
import random

# Create your views here.


def cookies(request):
    cookies = Cookies.objects.all()
    privacy = Privacy.objects.all()

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    COOKIES_PRIVACY_PRIVACY_ = {'facebook': facebook, 'email': email, 'cookies': cookies, 'privacy': privacy}

    args = COOKIES_PRIVACY_PRIVACY_

    return render(request, 'cookies/cookies.html', args)

