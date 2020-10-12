"""Defines URL patterns for retail_app"""

from django.urls import path

from .views import index, search, filters

app_name = "retail_app"

urlpatterns = [
    # Home
    path("", index, name="index"),
    # Search results
    path("search/", search, name="search"),
    # Filter results
    path("filters/", filters, name="filters"),
]
