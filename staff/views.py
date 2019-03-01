# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import BackgroundImage, FacebookLink, EmailLink
from staff.models import Role, Staff_Bio
import random

# Create your views here.

def get_staff(request):
    staff = Staff_Bio.objects.all()
    roles = Role.objects.all().order_by('rank')

    count = BackgroundImage.objects.filter(active=True).count()
    rand = random.randint(1, count)
    background = BackgroundImage.objects.filter(active=True).get(pk=rand)

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    args = {
        'facebook': facebook,
        'email': email,
        'background': background,
        'staffs': staff,
        'roles': roles
    }

    return render(request, 'staff/staff_profiles.html', args)