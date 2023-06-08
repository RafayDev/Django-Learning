"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mysite import views
from mysite import profiles
from mysite.controllers import test
from mysite.controllers import item
from mysite.controllers import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about-us/', views.aboutus, name='aboutus'),
    path('profiles', profiles.api_view2, name='profiles'),
    path('test', test.index, name='test'),
    path('items/', item.getitem, name='items'),
    path('additem/', item.additem, name='additem'),
    path('updateitem/', item.updateitem, name='updateitem'),
    path('deleteitem/', item.deleteitem, name='deleteitem'),
    path('getitembyid/', item.getitembyid, name='getitembyid'),
    path('register_user/', user.register_user, name='register_user'),
    path('login_user/', user.login_user, name='login_user'),
]

