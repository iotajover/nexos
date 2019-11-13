from .models import Studen
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.AutoField()
    name = serializers.CharField(max_length=512)