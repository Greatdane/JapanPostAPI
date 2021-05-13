from rest_framework import serializers
from .models import International_Parcel_Post, Country

class Country_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class International_Parcel_Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = International_Parcel_Post
        fields = '__all__'

