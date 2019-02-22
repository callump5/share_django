# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from home.models import BackgroundImage, FacebookLink, EmailLink
from .models import FileUpload


import random


# Create your views here.

def get_policies(request):

    count = BackgroundImage.objects.filter(active=True).count()
    rand = random.randint(1, count)
    background = BackgroundImage.objects.filter(active=True).get(pk=rand)

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    uploadfiles = FileUpload.objects.all()


    args = {
        'facebook': facebook,
        'email': email,
        'background': background,
        'files': uploadfiles,
    }

    return render(request, 'policies/policy_files.html', args)

