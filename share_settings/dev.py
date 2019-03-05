from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
from aws_login import *

import aws_login

AWS_ACCESS_KEY_ID = aws_login.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = aws_login.AWS_SECRT_ACCESS_KEY


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Keys

if DEBUG == False:

    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRT_ACCESS_KEY = os.getenv('AWS_SECRT_ACCESS_KEY')
    stripe.api_key = os.getenv('stripe.api_key')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')

    # Recaptcha

    GOOGLE_RECAPTCHA_SECRET_KEY = os.getenv('GOOGLE_RECAPTCHA_SECRET_KEY')
