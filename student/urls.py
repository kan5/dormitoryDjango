
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='st_profile'),
    path('in_form', views.in_form, name='in_form'),
    path('out_form', views.out_form, name='out_form'),
]
