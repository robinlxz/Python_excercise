from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Question(models.Model):
  question_text = models.CharField(max_length=200, unique=True)
  def __str__(self):
    return self.question_text

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=100)
  choice_chips = models.IntegerField(validators=[MinValueValidator(0)])
  def __str__(self):
    return self.choice_text

class User(models.Model):
  username = models.CharField(max_length=100, unique=True)
  user_chips = models.IntegerField(validators=[MinValueValidator(0)], default=0)
  def __str__(self):
    return self.username