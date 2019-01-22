# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import BackgroundImage, FacebookLink, EmailLink
from fundraising.models import FundraisingTarget, Donations

import random

# Create your views here.


def get_fundraising(request):


    count = BackgroundImage.objects.filter(active=True).count()

    rand = random.randint(1, count)

    background = BackgroundImage.objects.filter(active=True).get(pk=rand)

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    targets = FundraisingTarget.objects.all()
    donations = Donations.objects.all()


    args = {

        'facebook': facebook,
        'email': email,

        'background': background,

        'targets': targets,
        'donations': donations

    }

    return render(request, 'fundraising/fundraising.html', args)