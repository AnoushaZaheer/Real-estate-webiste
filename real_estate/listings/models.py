
from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    num_rooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    num_kitchens = models.IntegerField()
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.title
