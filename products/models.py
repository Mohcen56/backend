# products/models.py
from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    popularity_score = models.FloatField()
    weight = models.FloatField()
    image_yellow = models.URLField()
    image_rose = models.URLField()
    image_white = models.URLField()

    def __str__(self):
        return self.name


