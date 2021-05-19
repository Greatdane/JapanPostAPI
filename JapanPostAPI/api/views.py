# from django.shortcuts import render
from rest_framework import generics

from .models import Country
from .serializers import Country_Serializer


class CountryAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = Country_Serializer