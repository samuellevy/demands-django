from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .views import (
    demands_index,
)

urlpatterns = [
    url(r'^$', demands_index),
]

# url(r'^anything$') is the same path(anything)