from .models import Task, SubTask
from django import forms


class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['task_name']