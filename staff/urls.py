from django.conf.urls import url
from staff.views import get_staff

urlpatterns = [
    url(r'^staff-profiles/$', get_staff, name='staff')
]