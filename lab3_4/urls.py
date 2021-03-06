"""lab3_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from hello.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('route/borisov-minsk/', borisov_minsk),
    path('route/minsk-borisov/', minsk_borisov),
    path('register/', register),
    path('login/', user_login),
    path('logout/', user_logout),
    path('crud/', bus_form, name='bus_insert'),
    path('crud/list/', bus_list, name='bus_list'),
    path('crud/<int:id>/', bus_form, name='bus_update'),
    path('crud/delete/<int:id>', async_delete, name='bus_delete'),
]
