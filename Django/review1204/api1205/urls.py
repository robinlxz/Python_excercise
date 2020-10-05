from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
  path('api/todo/', views.TodoItemList.as_view() ),
  path('', views.index, name='index'),
  path('<int:item_id>/', views.detail, name='detail')
]