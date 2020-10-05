from django.db import models

# Create your models here.
class Team(models.Model):
  team_name = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.team_name

class Question(models.Model):
  question_text = models.CharField(max_length=200, unique=True)
  question_info = models.CharField(max_length=200, default='', blank=True)

  def __str__(self):
    return self.question_text

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200, unique=True)
  choice_odd = models.FloatField(default=0)

  def __str__(self):
    return self.choice_text