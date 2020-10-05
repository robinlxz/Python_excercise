from django.db import models

# Create your models here.
class Choice(models.Model):
  choice_text = models.CharField(max_length=200, unique=True)
  teamA_bet = models.IntegerField(default=0)
  teamB_bet = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text