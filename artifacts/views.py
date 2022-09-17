from django.shortcuts import render
from rest_framework import viewsets

from artifacts.models import Artifact
from artifacts.serializers import ArtifactSerializer


# bundle get, post, put, delete... with several view methods to a model
# it needs a serializer to convert the data into JSON and a queryset to get the data
class ArtifactViewSet(viewsets.ModelViewSet):
    serializer_class = ArtifactSerializer

    def get_queryset(self):
        return Artifact.objects.all()
