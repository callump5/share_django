# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from home.models import SlideImage
from home.models import HomeTitle, FacebookLink, EmailLink
from staff.models import Role, Staff_Bio
import random

# Create your views here.

def get_staff(request):

    staff = Staff_Bio.objects.all()
    roles = Role.objects.all().order_by('rank')


    title = HomeTitle.objects.get(pk=1)
    slides = SlideImage.objects.all()
    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    args = {
        'title': title,
        'slides': slides,
        'facebook': facebook,
        'email': email,
        'staffs': staff,
        'roles': roles
    }

    return render(request, 'staff/staff_profiles.html', args)