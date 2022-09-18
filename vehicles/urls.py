from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import tools, vehicles

router = DefaultRouter()
# Bind multiple viewsets to the same router
router.register(r"vehicles", vehicles.VehicleViewSet, "vehicle")
router.register(r"parts", vehicles.PartViewSet, "part")

urlpatterns = [
    path("", include(router.urls)),
    path("list_tools/", tools.list_tools),  # call our custom view
]