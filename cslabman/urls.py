"""Cslabman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import Statement
from django.urls import path
from . import views


# Base User view in Requests_Homepage Directory views.py
# URL Paths taking users to different parts of the website.

urlpatterns = [
    path('', views.home, name='Request-Home'),
    path('help/', views.help, name='Request-Help'),


]

