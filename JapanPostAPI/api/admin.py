from django.contrib import admin
from .models import Country, International_Parcel_Post, EMS, Small_Packet

admin.site.register(Country)
admin.site.register(International_Parcel_Post)
admin.site.register(EMS)
admin.site.register(Small_Packet)