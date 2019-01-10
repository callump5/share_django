from django.conf.urls import url

from .views import contact_us
urlpatterns = [
    url(r'^contact-us/$', contact_us)
]