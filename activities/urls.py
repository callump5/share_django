from django.conf.urls import url
from .views import get_activities

urlpatterns = [
    url(r'activities/$', get_activities, name='activities')
]