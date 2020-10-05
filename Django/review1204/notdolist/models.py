from django.db import models

# Create your models here.
class NotdoItem(models.Model):
  notdo_name = models.CharField(max_length=200, unique=True)
  start_time = models.DateTimeField(auto_now=True)
  notdo_description = models.CharField(max_length=200, default="Put reasons here.")

  def __str__(self):
    return self.notdo_name