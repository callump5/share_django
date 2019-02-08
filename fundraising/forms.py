from django import forms
from .models import Donations


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donations
        fields = ('donation', 'target', 'stripe_id')


    MONTHS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]

    MONTH_CHOICES = list(enumerate(MONTHS, 1))
    YEAR_CHOICES = [(i, i) for i in range(2016, 2027)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='CVV')
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


