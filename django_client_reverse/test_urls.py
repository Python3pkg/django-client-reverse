from django.conf.urls import url
from django_client_reverse.views import Reverser

urlpatterns = [
    url(r'^$', Reverser.as_view(), name="root"),
    url(r'(?P<uuid>[0-9a-f-]+)/$', Reverser.as_view(), name="uuid")
]
