from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^\?search=(?P<search>)$', views.index, name='search')
]
