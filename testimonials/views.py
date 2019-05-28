# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import HomeTitle, SlideImage
from testimonials.models import Testimonial
from home.models import BackgroundImage, FacebookLink, EmailLink

import random
# Create your views here.


def get_testimonials(request):


    title = HomeTitle.objects.get(pk=1)
    slides = SlideImage.objects.all()
    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    testimonial_list = Testimonial.objects.all()

    args = {
        'title': title,
        'slides': slides,
        'facebook': facebook,
        'email': email,
        'list': testimonial_list
    }

    return render(request, 'testimonials/list.html', args)