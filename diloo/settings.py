"""
Django settings for diloo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
<<<<<<< HEAD
=======

>>>>>>> e64198d1ec8ab66b34da6f833eb5cba7f22bea9f
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
import dj_database_url




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = 'c*ke_xvlnlh_-5mu10mabu18-!bq^9lvufbx1*hm&kg)ms46ll'
=======
SECRET_KEY = '4tai=ja=n=6^lqd4+0m=7$*u$+*ci#2t#tnxsy8&8-7hq6(ofn'
>>>>>>> e64198d1ec8ab66b34da6f833eb5cba7f22bea9f

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
<<<<<<< HEAD
    'south', 
=======
    'app.templatetags',
>>>>>>> e64198d1ec8ab66b34da6f833eb5cba7f22bea9f
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'diloo.urls'

WSGI_APPLICATION = 'diloo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "diloodb",
        "USER": "root",
        "PASSWORD": "n0m3l0",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
DATABASES['default'] =  dj_database_url.config()

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

<<<<<<< HEAD
LANGUAGE_CODE = 'en-mx'
=======
LANGUAGE_CODE = 'en-us'
>>>>>>> e64198d1ec8ab66b34da6f833eb5cba7f22bea9f

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'app/static'),
)
<<<<<<< HEAD
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'c*ke_xvlnlh_-5mu10mabu18-!bq^9lvufbx1*hm&kg)ms46ll'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# TEMPLATE_DEBUG = True

# ALLOWED_HOSTS = ['*']

# # Database
# # https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# # Application definition

# INSTALLED_APPS = (
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.messages',
#     'django.contrib.sessions',
#     'django.contrib.staticfiles',
#     'django.contrib.humanize',
#     'south',
#     'app',
# )
# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# )

# ROOT_URLCONF = 'diloo.urls'

# WSGI_APPLICATION = 'diloo.wsgi.application'



# # Internationalization
# # https://docs.djangoproject.com/en/1.6/topics/i18n/

# LANGUAGE_CODE = 'es-mx'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.6/howto/static-files/

# STATIC_URL = '/static/'


# TEMPLATE_DIRS = {
#      os.path.join(BASE_DIR, 'app/templates'),
# }
=======

# try:
#     from local_settings import * 
# except ImportError:
#     pass



















>>>>>>> e64198d1ec8ab66b34da6f833eb5cba7f22bea9f
