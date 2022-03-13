from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    delete = serializers.BooleanField(required=False, read_only=True)
    name = serializers.CharField()
    telephone = serializers.CharField()
    ddd = serializers.CharField()
