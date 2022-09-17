from rest_framework import serializers
from .models import Person


# Serializers specify how to turn the model into the payload data for rest
# ModelSerializer knows how to convert all the fields in the model into JSON
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "first", "last", "title"]
