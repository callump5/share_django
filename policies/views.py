# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from home.models import HomeTitle, SlideImage, FacebookLink, EmailLink
from .models import FileUpload

# Create your views here.

def get_policies(request):

    title = HomeTitle.objects.get(pk=1)
    slides = SlideImage.objects.all()
    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    uploadfiles = FileUpload.objects.all()

    args = {
        'title': title,
        'slides': slides,
        'facebook': facebook,
        'email': email,
        'files': uploadfiles,
    }

    return render(request, 'policies/policy_files.html', args)

