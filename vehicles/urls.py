from django.urls import path, include

from .views import tools

urlpatterns = [
    path("list_tools/", tools.list_tools),  # call our custom view
]