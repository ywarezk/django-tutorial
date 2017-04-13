from django.db import models

# Create your models here.
class Greeting(models.Model):
    message = models.CharField(max_length=300)
    user = models.CharField(max_length=100, blank=True)