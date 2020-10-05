from django.db import models

# Create your models here.
class Task(models.Model):
  task_name = models.CharField(max_length=100, unique=True, blank=False)
  pub_date = models.DateTimeField(auto_now=True)
  task_importance = models.IntegerField(default=1)

  def __str__(self):
    return self.task_name

class SubTask(models.Model):
  task = models.ForeignKey(Task, on_delete=models.CASCADE)
  subtask_name = models.CharField(max_length=200)

  def __str__(self):
    return self.subtask_name