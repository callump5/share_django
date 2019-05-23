# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import HomeTitle, SlideImage, HomeBox, HomeContent, FacebookLink, EmailLink, BackgroundImage
from contact_us.forms import ContactRequestForm
from django.contrib import messages


import random


# Create your views here.

def get_home(request):
    count = BackgroundImage.objects.filter(active=True).count()

    rand = random.randint(1, count)

    title = HomeTitle.objects.get(pk=1)
    slides = SlideImage.objects.all()
    info_boxes = HomeBox.objects.all()
    content = HomeContent.objects.all()

    background = BackgroundImage.objects.filter(active=True).get(pk=rand)

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    if request.method == 'POST':
        contact_form = ContactRequestForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            return redirect('services')
        else:
            contact_form = ContactRequestForm()
    else:
        contact_form = ContactRequestForm


    args = {

        'facebook': facebook,
        'email': email,

        'background': background,

        'title': title,
        'slides': slides,
        'info_boxes': info_boxes,
        'content': content,
    }

    return render(request, 'home/home.html', args)
