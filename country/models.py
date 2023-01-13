from django.db import models
from django.contrib.auth import get_user_model

class Country(models.Model):
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    country=models.CharField(max_length=255)
    weather=models.TextField(blank=True)
    longitude=models.FloatField()
    latitude=models.FloatField()
    def __str__(self):
        return self.country
