from django.conf.urls import url
import blog2.views

urlpatterns = [
    url(r'^$', blog2.views.index),
]
