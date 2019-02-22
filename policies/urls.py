from django.conf.urls import url
from policies.views import get_policies

urlpatterns = [
    url(r'^policies/$', get_policies, name='policies')
]