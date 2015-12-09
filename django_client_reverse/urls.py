from django.conf.urls import include, url
from .views import Reverser
from os import environ
from . import test_urls

urlpatterns = [
    url(r'^$', Reverser.as_view(), name="reverser")
]

if environ.get('IN_URL_TEST', False):
    urlpatterns += [
        url(r'^tests/', include(test_urls, namespace="tests"))
    ]
