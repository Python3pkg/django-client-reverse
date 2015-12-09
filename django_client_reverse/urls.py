from django.conf.urls import include, url
from .views import Reverser
urlpatterns = [
    url(r'^$', Reverser.as_view(), name="reverser")
]
