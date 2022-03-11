from turtle import pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ContactSerializer
from .models import Contact
import pdb

import json

class CreateContact(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        contact_exist = Contact.objects.filter(telephone=data["telephone"]).exists()
        if contact_exist:
            return Response({"Error": "This telephone already exist"}, status=status.HTTP_409_CONFLICT)

        contact = Contact.objects.create(**data)

        serializer = ContactSerializer(data=contact.__dict__)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serialized = serializer.data
        serialized['id'] = contact.id
        return Response(serialized, status=status.HTTP_201_CREATED)

    def put(self, request, contact_id=None):
        contact = Contact.objects.get(id=contact_id)
        for key in request.data:
            if contact.__dict__[key] and not key == "id":
                contact.__dict__[key] = request .data[key]
        contact.save()
        serializer = ContactSerializer(data=contact.__dict__)

        if not serializer.is_valid():       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, contact_id=None):
        try:
            contact = Contact.objects.get(id=contact_id)
        except:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        contact.deleted = True
        contact.save()
        serializer = ContactSerializer(data=contact.__dict__)

        if not serializer.is_valid():       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({}, status=status.HTTP_200_OK)

    def get(self, request, contact_id=None):
        contact = Contact.objects.all()
        return Response([ContactSerializer(cont).data for cont in contact], status=status.HTTP_200_OK)



