from .models import International_Parcel_Post, Country
from rest_framework import viewsets, permissions
from .serializers import International_Parcel_Post_Serializer, Country_Serializer

class Country_Viewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = Country_Serializer

class International_Parcel_Post_ViewSet(viewsets.ModelViewSet):
    queryset = International_Parcel_Post.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = International_Parcel_Post_Serializer
