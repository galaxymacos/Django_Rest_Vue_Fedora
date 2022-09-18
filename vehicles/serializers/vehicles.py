from rest_framework import serializers

from ..models import Vehicle, Part


class SerialNumberField(serializers.CharField):  # The custom field inherits from CharField
    # Create a custom serializer field
    def to_representation(self, value):  # value is the model instance -> Part
        code = value.make[:3].upper()
        return f"{code}-{value.id}"


class PartSerializer(serializers.ModelSerializer):
    # source="*" passes the model instance to the field to use in to_representation
    serial_no = SerialNumberField(source="*")

    class Meta:
        model = Part
        fields = ["url", "name", "vehicle", "serial_no"]


class VehicleSerializer(serializers.ModelSerializer):
    part_set = PartSerializer(many=True, read_only=True)    # vehicle to part is a one-to-many relationship

    class Meta:
        model = Vehicle
        fields = ["url", "name", "part_set"]    # url is the detail view url, allows quick navigation in browsable API
