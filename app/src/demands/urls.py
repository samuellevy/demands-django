from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
    demands_index,
    demands_create
)

urlpatterns = [
    url(r'^$', demands_index),
    path('index/', demands_index),
    path('create/', demands_create)
]

# url(r'^anything$') is the same path(anything)