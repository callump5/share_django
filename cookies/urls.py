from django.conf.urls import url


import views


urlpatterns = [
    url(r'^privacy-cookies-policy/$', views.cookies),
]