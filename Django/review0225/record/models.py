from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(models.Model):
  name = models.CharField(unique=True, max_length=100)
  age = models.IntegerField(blank=True, validators=[
    MinValueValidator(0), MaxValueValidator(120)
  ])

class Symptom(models.Model):
  person = models.ForeignKey(Person, on_delete=models.CASCADE)
  symptom_text = models.CharField(max_length=200)