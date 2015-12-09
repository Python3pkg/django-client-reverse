import os

import dj_database_url
DATABASES = {'default': dj_database_url.config(default="sqlite://memory")}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django_client_reverse'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SECRET_KEY = 'abcde12345'

ROOT_URLCONF = 'django_client_reverse.urls'
