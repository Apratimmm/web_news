from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[
    path('',views.firsthome),
    path('news/',views.home)
]