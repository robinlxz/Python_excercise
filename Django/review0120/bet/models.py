from django.db import models

# Create your models here.
class Team(models.Model):
  team_name = models.CharField(unique=True, max_length=100, default='')
  team_bet = models.IntegerField(default=0)