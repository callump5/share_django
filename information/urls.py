from django.conf.urls import url

from .views import get_info

urlpatterns = [
    url('^info/$',get_info, name='info')
]