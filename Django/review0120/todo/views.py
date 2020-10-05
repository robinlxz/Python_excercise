from django.shortcuts import render
from django.views import View

# Create your views here.
from .models import Task, SubTask
from .forms import TaskForm

def index(request):
  task_list = Task.objects.all()
  form = TaskForm(request.POST)
  if form.is_valid():
    form.save()
  context = {
    'task_list': task_list,
    'form': form
  }
  return render(request, 'todo/todo_index.html', context)




class TaskView(View):
  def get(self, request, task_id):
    task = Task.objects.get(pk=task_id)
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
    context = {
    'task': task,
    'form': form
    }
    return render(request, 'todo/task_detail.html', context)

  def post(self, request, task_id):
    task = Task.objects.get(pk=task_id)
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
    context = {
    'task': task,
    'form': form
    }
    return render(request, 'todo/task_detail.html', context)