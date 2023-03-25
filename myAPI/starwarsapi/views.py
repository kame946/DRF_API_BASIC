from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SpeciesSerializer, PersonSerializer
from .models import Species, Person
# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

