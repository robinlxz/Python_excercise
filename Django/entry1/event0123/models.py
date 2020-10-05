from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Question(models.Model):
  question_text = models.CharField(max_length=200, unique=True)
  question_lock = models.BooleanField(default=False)
  # question_info = models.CharField(max_length=200, default='', blank=True)

  def __str__(self):
    return self.question_text

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200, unique=True)
  choice_odd = models.FloatField(default=0)
  choice_bet = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text  

class User(models.Model):
  user_name = models.CharField(max_length=100, unique=True)
  user_chips = models.IntegerField(default=0, validators=[MinValueValidator(0)])
  # Need a better field for bet history
  user_bet_history = models.TextField(default='', blank=True)

  def __str__(self):
    return self.user_name
