from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Keys

if DEBUG:

    from aws_login import *

    from aws_login import AWS_SECRT_ACCESS_KEY as AWS_KEY
    from aws_login import AWS_ACCESS_KEY_ID as AWS_ID


    AWS_ACCESS_KEY_ID = AWS_ID
    AWS_SECRET_ACCESS_KEY = AWS_KEY

else:

    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

    stripe.api_key = os.getenv('stripe.api_key')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')

    GOOGLE_RECAPTCHA_SECRET_KEY = os.getenv('GOOGLE_RECAPTCHA_SECRET_KEY')
