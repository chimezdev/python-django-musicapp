"""songcrud URL Configuration

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
from . import views #imports views do we can use it
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), #empty '' means that is the root url
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login')
]
#'views.index' above means, when a user visits that url, what to render is found in the 'views.index'
# the 'name=index' is just a tag, it could be named anything but bcos homepage is usually named index file

