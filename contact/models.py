from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ContactList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200 , null=True)
    email = models.EmailField(max_length = 254 , unique=True)
    Phoneno = models.CharField(max_length = 20)
    Mobileno = models.CharField(max_length=20 , blank=True)
    