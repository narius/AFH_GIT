"""AFH_live URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from session12live.views import index
from session13live.views import vote, new_answer, new_question, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vote, name='index'),
    path('something/vote/<int:answer_pk>', vote, name='vote'),
    path('new_question', new_question, name='new_question'),
    path('new_answer', new_answer, name='new_answer'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout')
]
