from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^update/(?P<data_id>[0-9]+)$', FileUpdateView.as_view()),
    url(r'^create$', FileUpdateView.as_view())
]