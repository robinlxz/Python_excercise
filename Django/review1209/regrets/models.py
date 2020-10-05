from django.db import models

# Create your models here.
class Behavior(models.Model):
  title = models.CharField(max_length=200, unique=True)
  text = models.CharField(max_length=400, help_text="What have you done?")
  consequence = models.CharField(max_length=400, help_text="What is the consequence?", default='') 
  timestamp = models.DateTimeField(auto_now=True, verbose_name='When')
  counts = models.IntegerField(help_text='It happens for how many times?', default=0)

  def __str__(self):
    return self.title