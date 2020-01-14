from django.db import models

# Create your models here.
class Question(models.Model):
  question_text = models.CharField(max_length=200, unique=True)
  pub_date = models.DateField(auto_now=True)

  def __str__(self):
    return self.question_text

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  vote = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text


class Snippet(models.Model):
  name = models.CharField(max_length=100)
  body = models.TextField()

  def __str__(self):
    return self.name