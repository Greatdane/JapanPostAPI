from rest_framework import routers
from .api import International_Parcel_Post_ViewSet, Country_Viewset

from django.urls import path, include
from .views import CountryAPIView

urlpatterns = [
    path('api/country', CountryAPIView.as_view())
]