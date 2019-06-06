# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from contact_us.models import OpenTimes, StaffContact
from contact_us.forms import ContactRequestForm
from .models import HomeTitle, SlideImage, HomeBlurb, AboutUs, FacebookLink, EmailLink
from contact_us.forms import ContactRequestForm
from django.contrib import messages


import random


# Create your views here.

def get_home(request):

    title = HomeTitle.objects.get(pk=1)
    slides = SlideImage.objects.all()
    info_boxes = HomeBlurb.objects.all()
    content = AboutUs.objects.all()


    contacts = StaffContact.objects.all()
    open = OpenTimes.objects.all()

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
        'open': open,
        'form': contact_form,
        'contacts': contacts,

        'title': title,
        'slides': slides,
        'info_boxes': info_boxes,
        'content': content,
    }

    return render(request, 'home/home.html', args)
