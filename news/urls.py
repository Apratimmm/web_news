from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[
    path('',views.initalhome),
    path('news/',views.home),
    path('search/', views.search, name='search'),
]