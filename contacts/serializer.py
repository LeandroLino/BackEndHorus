from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    telephone = serializers.CharField()
    ddd = serializers.CharField()
