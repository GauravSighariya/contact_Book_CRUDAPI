from django.views.generic import TemplateView
from django.urls import path,re_path, include
from .views import Contact, ContactDeleteUpdate
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Contact API')
urlpatterns = [
    re_path(r'^$', Contact.as_view(), name='Add Contact'),
    re_path(r'^(?P<id>[0-9]*)$', ContactDeleteUpdate.as_view(), name='Contact Update Delete'),
    url(r'^$', schema_view)
]