# from django.shortcuts import render
from rest_framework import generics, filters

from .models import Country
from .serializers import Country_Serializer


class CountryAPIView(generics.ListCreateAPIView):
    search_fields = ['country_en']
    filter_backends = [filters.SearchFilter]
    queryset = Country.objects.all()
    serializer_class = Country_Serializer
