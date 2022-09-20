import imp
from django.shortcuts import render
from .models import ContactList
from .serializers import ContactListDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend


class Contact(APIView):
    
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        contact = ContactList.objects.filter(user=request.user)
        serializer = ContactListDetailSerializer(contact, many=True)
        filterset_fields = ['id','first_name','email']
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactListDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactDeleteUpdate(APIView):
    """
    Delete and  update server.
    """
    def get_object(self, id):
        try:
            return ContactList.objects.get(id=id)
        except ContactList.DoesNotExist:
            raise Http404

    permission_classes = (IsAuthenticated,)
    def put(self, request,id,format=None):
        loadeddata= self.get_object(id)
        print(loadeddata, request.data)
        serializer = ContactListDetailSerializer(loadeddata,data=request.data,partial=True)
        if serializer.is_valid():
            print("yes")
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id, format=None):
        loadeddata = self.get_object(id)
        loadeddata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)