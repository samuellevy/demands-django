from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    path('create/', views.post_create)
]

# url(r'^anything$') is the same path(anything)