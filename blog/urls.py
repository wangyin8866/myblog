from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^create/(?P<article_id>[0-9]+)$', views.article_edit, name='article_edit'),
    url(r'^edit/$', views.article_edit_action, name='article_edit_action'),
    url(r'^delete/(?P<article_id>[0-9]+)$', views.article_delete, name='article_delete'),
]
