from django.conf.urls import url


from .views import get_staff


urlpatterns = [
    url(r'^staff/$', get_staff),
]
