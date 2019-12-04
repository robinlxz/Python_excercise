from django.db import models

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=200, unique=True)