from django.db import models

# Create your models here.
class Skill(models.Model):
  name = models.CharField(max_length=100, unique=True)
  create_time = models.DateTimeField(auto_now=True)
  skill_point = models.IntegerField(default=0)

  def __str__(self):
    return self.name
