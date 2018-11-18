# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import HomeTitle, SlideImage, HomeBox, HomeContent, FacebookLink, EmailLink

# Create your views here.

def get_home(request):

    title = HomeTitle.objects.get(pk=1)
    slides = SlideImage.objects.all()
    info_boxes = HomeBox.objects.all()
    content = HomeContent.objects.all()

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    args = {

        'facebook': facebook,
        'email': email,

        'title': title,
        'slides': slides,
        'info_boxes': info_boxes,
        'content': content,
    }

    return render(request, 'home/home.html', args)
