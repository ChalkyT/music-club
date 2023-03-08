"""albumclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from albumclub.spa.views import SpaView
# from albumclub.api.views import GreetingApi
from albumclub.api import views #this imports the views from views.py for the api app
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('api/greet', GreetingApi.as_view()),
    path("", SpaView.as_view(), name="spa"),
    path('api/albums/', views.all_albums), #passing in the all_albums function 
    path('api/albums/<int:id>', views.album_detail), #adding parameter of type 'int' this will link up with album_detail function in view.py
]

urlpatterns = format_suffix_patterns(urlpatterns)
#