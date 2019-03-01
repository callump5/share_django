# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from smtplib import SMTPAuthenticationError
from .forms import ContactRequestForm
from .models import StaffContact
from .send_email import send_contact_request, authError
from home.models import BackgroundImage, EmailLink, FacebookLink
import random

import requests
from share_django.settings import GOOGLE_RECAPTCHA_SECRET_KEY as GRK

from django.contrib import messages


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


            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': GRK,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                contact = contact_form.save()
                contact.save()
                messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
                try:
                    send_contact_request(request, contact.name, contact.email, contact.number, contact.text)
                except SMTPAuthenticationError:
                    authError(request)
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('/contact-us')




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