from django.contrib import admin
from django.conf.urls import include, url
from .views import home, register

urlpatterns =[
    url(r'^$',home),
    url(r'^register/',register),
]