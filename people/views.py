from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer


@api_view(["GET"])
def list_people(request):
    people = Person.objects.all()  # Get all the people
    serializer = PersonSerializer(people, many=True)  # Serialize people
    content = {"people": serializer.data}  # Create a dictionary with the serialized people
    return Response(content)  # Return the serialized data
 