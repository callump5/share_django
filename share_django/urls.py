"""share_django URL Configuration

The `urlpatterns` list routes URLs to views. For more info please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from django.contrib import admin

from .settings import STATIC_ROOT, MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Static
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

    # Media Root
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # TINYMCE
    url(r'', include('tinymce.urls')),

    # Home Urls
    url(r'', include('home.urls')),

    # Information Urls
    url(r'', include('information.urls')),

    # Testimonials
    url(r'', include('testimonials.urls')),

    # Staff
    url(r'', include('staff.urls')),

    # Contact
    url(r'', include('contact_us.urls')),

    # Fundraising
    url(r'', include('fundraising.urls'))

]
