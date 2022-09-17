from django.urls import path

from people import views

urlpatterns = [
    path("list_people/", views.list_people),
]
