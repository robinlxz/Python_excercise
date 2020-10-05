from django.db import models

# Create your models here.
class TodoItem(models.Model):
  todo_name = models.CharField(max_length=100, unique=True)
  start_date = models.DateTimeField(auto_now=True)
  todo_description = models.CharField(max_length=200, default='Reason for todo')

  def __str__(self):
    return self.todo_name