from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:task_id>', views.TaskView.as_view(), name='task_detail'),
]