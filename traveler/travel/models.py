from django.db import models

# Create your models here.
class Desinations(models.Model):
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    cities = models.IntegerField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
