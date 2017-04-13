"""
Definition of urls for FBWish.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from . import forms
from . import views


urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
   # url(r'^contact$', views.contact, name='contact'),
   # url(r'^about', views.about, name='about'),
    url(r'^profile', views.user_home, name='user_home'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'FBWish/login.html',
            'authentication_form': forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
]
