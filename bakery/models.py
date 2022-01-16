from django.db import models


# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(default=None)
    price = models.IntegerField(default=None)
    offer = models.BooleanField(default=False)


class SpecialOffers(models.Model):
    discount = models.IntegerField(default=None)
    name = models.CharField(max_length=100)
    desc = models.TextField(default=None)
