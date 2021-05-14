from django.db import models

class Country(models.Model):
    country_en = models.CharField(max_length=200)
    country_jp = models.CharField(max_length=200)
    zone_EMS = models.CharField(max_length=3, blank=True, null=True)
    zone_International_Parcel_Post = models.IntegerField()
    zone_Letter_Small_Packet = models.IntegerField()

    def __str__(self):
        return self.country_en

class International_Parcel_Post(models.Model):
    weight = models.IntegerField()
    zone = models.IntegerField()
    airmail_price = models.IntegerField()
    SAL_price = models.IntegerField()
    surface_price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class EMS(models.Model):
    weight = models.IntegerField()
    zone = models.CharField(max_length=3)
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)