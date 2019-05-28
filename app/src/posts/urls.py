from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete
)

urlpatterns = [
    url(r'^$', post_list),
    path('create/', post_create),
    url(r'^detail/$', post_detail),
    path('update/', post_update),
    path('delete/', post_delete),
]

# url(r'^anything$') is the same path(anything)