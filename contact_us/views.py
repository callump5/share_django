# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from smtplib import SMTPAuthenticationError
from .forms import ContactRequestForm
from .models import StaffContact
from .send_email import send_contact_request, authError
from home.models import BackgroundImage, EmailLink, FacebookLink
import random


# Create your views here.

def contact_us(request):

    count = BackgroundImage.objects.filter(active=True).count()

    rand = random.randint(1, count)

    background = BackgroundImage.objects.filter(active=True).get(pk=rand)

    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    contacts = StaffContact.objects.all()

    if request.method == 'POST':

        contact_form = ContactRequestForm(request.POST)

        if contact_form.is_valid():
            contact = contact_form.save()
            contact.save()

            try:
                send_contact_request(request, contact.name, contact.email, contact.number, contact.text)
            except SMTPAuthenticationError:
                authError(request)

        return redirect('/')

    else:
        contact_form = ContactRequestForm()

    args = {

        'facebook': facebook,
        'email': email,

        'background': background,

        'form': contact_form,
        'contacts': contacts
    }

    return render(request, 'contact/contact-us.html', args)