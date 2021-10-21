"""core URL Configuration

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
#Import Statements
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views

#URL paths to take users to different parts of the website
urlpatterns = [

    #Admin page route
    path('admin/', admin.site.urls),


    #Custom view for login. NO django authentication support
    #path('login/', users_views.register, name='register'),

    #django authentication enabled login view.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    #django authentication enabled logout view
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),


    # Access Request Questionnaire form
    path('MTCS-Requests/', users_views.mtcsRequests, name='MTCS-Requests'),

    #Standard user view page route
    path('', include('cslabman.urls')),


]
admin.site.site_header = "MTCS Admin"
admin.site.site_title = "MTCS Admin Portal"
admin.site.index_title = "Welcome to MTCS Admin Portal"