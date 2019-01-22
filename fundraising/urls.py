from django.conf.urls import url

from .views import get_fundraising
urlpatterns = [
    url(r'^fundraising/$', get_fundraising)
]