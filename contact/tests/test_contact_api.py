from urllib import response
from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from contact.views import Contact
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView


class ApiUrlTests(SimpleTestCase):
    def test_get_contacts_is_resolved(self):
        url = reverse('Add Contact')
        self.assertEquals(resolve(url).func.view_class, Contact)

class AddcontactwithoutToken(APITestCase):
    def test_addcontact(self):
        data = {'first_name':"testcase",'last_name':"yadav",'email':"gauravara@gmail.com",'Phoneno':"89438643",'Mobileno':"869058493"}
        response = self.client.post("/api/ky/server/",data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

class get_contact(APITestCase):
    list_url = reverse('Add Contact')
    def setUp(self):
        self.user = User.objects.create_user(username='davinci',password='admin@123')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
