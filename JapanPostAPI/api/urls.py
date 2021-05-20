from django.urls import path, include
from .views import CountryAPIView

urlpatterns = [
    path('api/country', CountryAPIView.as_view())
]