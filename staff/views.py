# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import StaffDetails
from home.views import BackgroundImage, EmailLink, FacebookLink

import random

# Create your views here.


# Staff View

def get_staff(request):
    count = BackgroundImage.objects.filter(active=True).count()
    rand = random.randint(1, count)
    background = BackgroundImage.objects.filter(active=True).get(pk=rand)

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()
    staff_list = StaffDetails.objects.all().order_by('role').reverse()

    args = {
        'facebook': facebook,
        'email': email,
        'background': background,
        'staff': staff_list
    }

    return render(request, 'staff/staff.html', args)
