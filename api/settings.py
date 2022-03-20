###############################################################################
# Filename: settings.py                                                        #
# Project: TomorrowNow                                                         #
# File Created: Friday March 4th 2022                                          #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Fri Mar 18 2022                                               #
# Modified By: Corey White                                                     #
# -----                                                                        #
# License: GPLv3                                                               #
#                                                                              #
# Copyright (c) 2022 TomorrowNow                                               #
#                                                                              #
# TomorrowNow is an open-source geospatial participartory modeling platform    #
# to enable stakeholder engagment in socio-environmental decision-makeing.     #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License            #
# along with this program.  If not, see <https://www.gnu.org/licenses/>.       #
#                                                                              #
###############################################################################


"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import environ
import os



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# https://django-environ.readthedocs.io/en/latest/
# Take environment variables from .env file
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)
# Initialise environment variables
environ.Env.read_env(os.path.join(BASE_DIR, 'api', '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'world.apps.WorldConfig',
    'grassapp.apps.GrassappConfig',
    'savana.apps.SavanaConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.gis",
    'corsheaders',
    'rest_framework',
    'rest_framework_gis',
    # 'guardian',
    'django_filters',
    'django_extensions',
    'debug_toolbar',
    'channels'
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Add Later
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend', # default
#     'guardian.backends.ObjectPermissionBackend',
# )


MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    import os  # only if you haven't already imported this
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']


CORS_ALLOWED_ORIGINS = [
    'http://localhost:8005',
    'http://actinia-core:8088',
    'http://localhost:3000',
]
# CORS_ORIGIN_ALLOW_ALL = True



# CORS_ALLOWED_ORIGIN_REGEXES are regular expressions that match domains 
# that can make requests. This setting is especially useful if you have many domains.
# CORS_ALLOWED_ORIGIN_REGEXES = [
# r"^https://\w+\.domain\.com$",
# r"^http://\w+\localhost\:3000$",
# r"^http://\w+\actinia-core\:8088$",
# ]

# The CORS_URLS_REGEX setting restricts which URLs the server will 
# send CORS headers to. It’s useful, for example, when you just want 
# to send headers on part of your site. Here’s an example:
# CORS_URLS_REGEX = r'^/api/.*$'


CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# CORS_EXPOSE_HEADERS is a list of headers exposed to the browser. 
# The default is an empty array.
CORS_EXPOSE_HEADERS = []

# Defines the time in seconds a browswer can cache a header response to a
# preflight request. Deafualts to 86,400 (one day)
CORS_PREFLIGHT_MAX_AGE = 86400 

# CORS_ALLOW_CREDENTIALS is a true or false value. So, its value determines whether the server 
# allows cookies in the cross-site HTTP requests.
CORS_ALLOW_CREDENTIALS=True


CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000'
    ]


ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env('POSTGRES_DBNAME'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT')
    }
}

# CACHES
# https://django-redis-cache.readthedocs.io/en/latest/intro_quick_start.html
# https://docs.djangoproject.com/en/4.0/topics/cache/
CACHES = {
    #  'default': {
    #     'BACKEND': 'redis_cache.RedisCache',
    #     'LOCATION': 'localhost:6379',
    # },
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis://{env("REDIS_USER")}:{env("REDIS_PASSWORD")}@django-redis-cache:6370',
        'OPTIONS': {
            'db': '10',
            'parser_class': 'redis.connection.HiredisParser',
            'pool_class': 'redis.BlockingConnectionPool',
        }
    }
}

# These are development values only never push to prod server.
ACTINIA = {
    #actinia-user create -r superadmin -u django-api -w c@kna663A -g api-super
    'user': 'django-api',
    'password': 'c@kna663A',
    'group': 'api-super',
    'role': 'superadmin',
    'HOST': 'actinia-core',
    'PORT': 8088,
    'ACTINIA_USER': env('ACTINIA_USER'),
    'ACTINIA_PASSWORD': env('ACTINIA_PASSWORD'),
    'ACTINIA_VERSION': env('ACTINIA_VERSION'),
    'ACTINIA_BASEURL': env('ACTINIA_BASEURL'),
    'ACTINIA_LOCATION': env('ACTINIA_LOCATION'),
    'ACTINIA_MAPSET': env('ACTINIA_MAPSET')
}
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Google Cloud Storage Settings
# https://django-storages.readthedocs.io/en/latest/backends/gcloud.html
# https://cloud.google.com/iam/docs/creating-managing-service-account-keys#iam-service-account-keys-create-gcloud
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = env('GS_BUCKET_NAME')
GS_PROJECT_ID = env('GS_PROJECT_ID')

STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Channels
ASGI_APPLICATION = "api.asgi.application"
