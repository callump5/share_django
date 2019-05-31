# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,reverse
from django.contrib import messages

from django.template.context_processors import csrf
import stripe
import stripe.error
from share_settings.staging import STRIPE_PUBLISHABLE_KEY

from home.models import HomeTitle, SlideImage, FacebookLink, EmailLink
from fundraising.models import Donations
from .forms import DonationForm
from.models import FundraisingTarget

import random

# Create your views here.


def get_fundraising(request):


    title = HomeTitle.objects.get(pk=1)
    slides = SlideImage.objects.all()
    facebook = FacebookLink.objects.all()
    email = EmailLink.objects.all()

    targets = FundraisingTarget.objects.all()
    donations = Donations.objects.all()


    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount= int(form.cleaned_data['donation'] * 100),
                    currency="GBP",
                    description= 'Share',
                    card= form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    new_form = form.save(False)

                    new_form.save()
                    messages.success(request, 'Thank you for your donation of £' + str(
                        float(form.cleaned_data['donation'])) + ' It is greatly appreciated!')

                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

            return redirect('home')
    else:
        form = DonationForm()


    args = {

        'title': title,
        'slides': slides,
        'facebook': facebook,
        'email': email,

        'targets': targets,
        'donations': donations,
        'donation_form': form,
        'publishable': STRIPE_PUBLISHABLE_KEY,

    }

    args.update(csrf(request))

    return render(request, 'fundraising/fundraising.html', args)



