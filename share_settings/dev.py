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

