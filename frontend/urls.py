from django.urls import path
from frontend.view import index
urlpatterns = [
    path("", index, name="frontend_index"),
]