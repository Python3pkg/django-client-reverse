from django.conf.urls import url
from django.http import HttpResponse


PASS_TEXT = "PASS"


def test_view(request, *args, **kwargs):
    return HttpResponse(PASS_TEXT)


urlpatterns = [
    url(r'^$', test_view, name="root"),
    url(r'(?P<uuid>[0-9a-f-]+)/$', test_view, name="uuid"),
    url(r'(?P<uuid>[0-9a-f-]+)/(?P<pk>[0-9a-f-]+)$', test_view, name="multi")
]
