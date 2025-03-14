from django.db import models


class Apartment(models.Model):
    title = models.CharField(max_length=255)
    rooms = models.CharField(max_length=20, null=True, blank=True)
    square = models.CharField(max_length=20, null=True, blank=True)
    price = models.FloatField()
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=100, null=True, blank=True)
    commission = models.CharField(max_length=20, null=True, blank=True)
    deposit = models.CharField(max_length=20, null=True, blank=True)
    link = models.URLField()

    def __str__(self):
        return self.title
    