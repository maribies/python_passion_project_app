"""Defines URL patterns for retail_app"""

from django.urls import path

from . import views

app_name = "retail_app"

urlpatterns = [
    # Home
    path("", views.index, name="index")
]
