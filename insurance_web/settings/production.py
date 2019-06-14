from .base import *

os.environ['SECRET_KEY'] = '$n_h@86s79l732jwht8a8sy2a7!c6@8wzqbgu62^kkz^um64ql'
#SECRET_KEY = os.environ['SECRET_KEY'] 
SECRET_KEY = '$n_h@86s79l732jwht8a8sy2a7!c6@8wzqbgu62^kkz^um64ql'
DEBUG = False
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# X_FRAME_OPTIONS = 'DENY'

ALLOWED_HOSTS += ["*"]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tkinsurancedb',
        'USER': 'tkinsurance',
        'PASSWORD': 'Pass@1234',
        'HOST': 'localhost',
        'PORT': '',
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