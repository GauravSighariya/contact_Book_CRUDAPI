from rest_framework import serializers
from .models import ContactList

class ContactListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactList
        fields = ('id','first_name','last_name','email','Phoneno','Mobileno' )