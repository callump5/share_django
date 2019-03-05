from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    from aws_login import AWS_ACCESS_KEY_ID as AWS_ID
    from aws_login import AWS_SECRT_ACCESS_KEY as AWS_KEY

    AWS_ACCESS_KEY_ID = AWS_ID
    AWS_SECRET_ACCESS_KEY = AWS_KEY

else:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
