from .views import Home
from django.urls import path

app_name = "config"
urlpatterns = [
    path("", Home, name="Home")
]
