from django.db import models

# Create your models here.
class Event(models.Model):
  event_name = models.CharField(max_length=200, unique=True)
  event_times = models.IntegerField(default=1)
  event_solution = models.CharField(max_length=400, default='')
  event_count = models.IntegerField(default=0)

  def __str__(self):
    return self.event_name

class Duty(models.Model):
  duty_name = models.CharField(max_length=200)
  count = models.IntegerField(default=0)
  
  def __str__(self):
    return self.duty_name

class SubDuty(models.Model):
  duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
  subduty_name = models.CharField(max_length=200, default='')

  def __str__(self):
    return self.subduty_name