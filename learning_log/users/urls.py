"""Defines URL patterns for users"""
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # Login page
    path(r'login/', LoginView.as_view(template_name='users/login.html'),
        name='login'),
    # Logout page
    url(r'logout/', views.logout_view, name='logout'),
    # Registration page
    url(r'register/', views.register, name='register'),
]