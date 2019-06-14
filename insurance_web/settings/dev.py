from .base import *

SECRET_KEY = '$n_h@86s79l732jwht8a8sy2a7!c6@8wzqbgu62^kkz^um64ql'
DEBUG = True
ALLOWED_HOSTS += ['mira',]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/tkinsurancestatic/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
MEDIA_URL = '/tkinsurancemedia/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
