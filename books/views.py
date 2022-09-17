from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission

from .models import Book
from .serializers import BookSerializer


# Give list permission and object permissions to all superusers
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


# Give rejected object permissions to indy
class IsIndy(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not obj.restricted:
            return True
        return request.user.username == "indy"


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsIndy | IsSuperUser]
    # The permission classes only apply to the detail view, not the list view

    # IsAuthenticated: Allow all users
    # IsAdminUser: Allow only admin users (including superuser, and staff)
    # IsSuperUser (Our custom permission): Allow only superuser

    def get_queryset(self):
        if self.request.user.is_staff:
            return Book.objects.all()
        else:
            # filter out restricted books in list view
            return Book.objects.filter(restricted=False)


# Set permission in request level
@login_required
def library(request):
    return render(request, "library.html")
