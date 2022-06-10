###############################################################################
# Filename: settings-dev.py                                                    #
# Project: TomorrowNow                                                         #
# File Created: Friday June 10th 2022                                          #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Fri Jun 10 2022                                               #
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


###############################################################################
# Filename: settings.py                                                        #
# Project: TomorrowNow                                                         #
# File Created: Friday March 4th 2022                                          #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Mon Jun 06 2022                                               #
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
    'channels',
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
    # 'oauth2_provider',
    'rest_framework',
    'rest_framework_gis',
    'guardian',
    'django_filters',
    'django_extensions',
    'debug_toolbar',
    'accounts'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication'
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated'
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Add Later
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)


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
    'http://localhost:5000',
    'http://192.168.1.242:3000',
    'http://localhost:7000',
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
    'content-range',
    'dnt',
    'origin',
    'range',
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
CORS_ALLOW_CREDENTIALS = True


CSRF_TRUSTED_ORIGINS = [
    'http://192.168.1.242:3000',
    'http://192.168.1.242:8005',
    'http://localhost:3000',
    'http://localhost:7000'
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
    },
    'actinia': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env('ACTINIA_POSTGRES_DBNAME'),
        'USER': env('ACTINIA_POSTGRES_USER'),
        'PASSWORD': env('ACTINIA_POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT')
    }
}

# CACHES
# https://django-redis-cache.readthedocs.io/en/latest/intro_quick_start.html
# https://docs.djangoproject.com/en/4.0/topics/cache/
# Running in Redis database 10
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
    # 'user': 'django-api',
    # 'password': 'c@kna663A',
    # 'group': 'api-super',
    # 'role': 'superadmin',
    # 'HOST': 'actinia-core',
    # 'PORT': 8088,
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
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    # os.path.join(BASE_DIR, 'static'),
    # os.path.join(BASE_DIR, "savana", "templates"),
    os.path.join(BASE_DIR, "world", "templates"),
    os.path.join(BASE_DIR, "grassapp", "static"),
    os.path.join(BASE_DIR, "grassapp", "templates")
]

STATIC_ROOT = "/var/www/tomorrownow/"
STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Channels
# Running in Redis database 5
ASGI_APPLICATION = "api.asgi.application"
CHANNEL_LAYERS = {
    'default': {
        # 'BACKEND': 'channels.layers.InMemoryChannelLayer',
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [f'redis://{env("REDIS_USER")}:{env("REDIS_PASSWORD")}@django-redis-cache:6370/5'],
        },
    },
}

# Celery
# Running in Databases 0 and 1
CELERY_BROKER_URL = f'redis://{env("REDIS_USER")}:{env("REDIS_PASSWORD")}@django-redis-cache:6370/0'
CELERY_RESULT_BACKEND = f'redis://{env("REDIS_USER")}:{env("REDIS_PASSWORD")}@django-redis-cache:6370/1'

# CELERY_TIMEZONE = "America/New_York"

# Django Extension Shell Plus Settings
SHELL_PLUS = "ipython"

SHELL_PLUS_PRINT_SQL = True

NOTEBOOK_ARGUMENTS = [
    "--ip",
    "0.0.0.0",
    "--port",
    "8010",
    "--allow-root",
    "--no-browser",
]

IPYTHON_ARGUMENTS = [
    "--ext",
    "django_extensions.management.notebook_extension",
    "--debug",
]

IPYTHON_KERNEL_DISPLAY_NAME = "Django Shell-Plus"

# extra things to import in notebook

SHELL_PLUS_POST_IMPORTS = [
    # ("module1.submodule", ("func1", "func2", "class1", "etc")),
    # ("module2.submodule", ("func1", "func2", "class1", "etc"))
]

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"  # only use in development
