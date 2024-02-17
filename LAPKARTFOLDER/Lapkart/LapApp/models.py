from django.db import models
# Create your models here.
class Lap_Model(models.Model):
    company = models.CharField(max_length=35)
    model = models.CharField(max_length=35)
    ram = models.IntegerField()
    rom = models.IntegerField()
    prices = models.FloatField()
