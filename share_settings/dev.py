from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


from aws_login import AWS_SECRT_ACCESS_KEY as AWS_KEY
from aws_login import AWS_ACCESS_KEY_ID as AWS_ID


AWS_ACCESS_KEY_ID = AWS_ID
AWS_SECRET_ACCESS_KEY = AWS_KEY


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
