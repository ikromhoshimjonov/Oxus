from django.contrib import admin
from django.urls import path

from home.views import HomeListApiView

urlpatterns = [
    path("list/home/",HomeListApiView.as_view()),
]
