from rest_framework import serializers


class ToolSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    name = serializers.CharField(max_length=50)
    make = serializers.CharField(max_length=50)
