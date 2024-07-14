from django.db import models

# Create your models here.

class Products(models.Model):
    """Respents a "user profile" inside our system."""
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    weight = models.FloatField()
    height = models.FloatField()
    altitude = models.IntegerField()
    endurance = models.IntegerField()
    wingspan = models.FloatField()
    payload = models.IntegerField()

