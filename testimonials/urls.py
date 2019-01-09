from django.conf.urls import url

from .views import get_testimonials


urlpatterns = [
    url('^testimonials/$',get_testimonials, name='testimonials')
]