"""Defines URL patterns for API"""

from django.urls import path

from .views import api

app_name = "api"

urlpatterns = [
    path("", api.get_data),
]
