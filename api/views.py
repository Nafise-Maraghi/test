from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


class PersonView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
