from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()    # create a router object
router.register(r'artifacts', views.ArtifactViewSet, "artifact")    # register the viewset with the router
urlpatterns = [
    path("", include(router.urls)),    # what urls does the router have?
]