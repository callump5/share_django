from base import *

DEBUG = False



AWS_ACCESS_KEY_ID = os.getenv('AWS_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_KEY')
GOOGLE_RECAPTCHA_SECRET_KEY = os.getenv('GOOGLE_RECAPTCHA_SECRET_KEY')

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}


# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}