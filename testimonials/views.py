# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from testimonials.models import Testimonial
from home.models import BackgroundImage, FacebookLink, EmailLink

import random
# Create your views here.


def get_testimonials(request):


    count = BackgroundImage.objects.filter(active=True).count()
    rand = random.randint(1, count)
    background = BackgroundImage.objects.filter(active=True).get(pk=rand)

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    testimonial_list = Testimonial.objects.all()

    args = {
        'facebook': facebook,
        'email': email,
        'background': background,
        'list': testimonial_list
    }

    return render(request, 'testimonials/list.html', args)