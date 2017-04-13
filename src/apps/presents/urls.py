"""
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PresentList.as_view(), name='present-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PresentDetail.as_view(), name='present-detail'),
    url(r'^create/', views.PresentCreate.as_view(), name='present-add'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.PresentUpdate.as_view(), name='present-edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.PresentDelete.as_view(), name='present-delete'),
]
