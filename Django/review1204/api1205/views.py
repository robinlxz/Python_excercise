from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import generics, permissions
from .models import TodoItem
from .serializers import TodoItemSerializer

def index(request):
  # return HttpResponse('Hello world 1205 API review')
  todo_list = TodoItem.objects.all()
  return render(request, 'todo/index.html', {'todo_list':todo_list})

def detail(request, item_id):
  item = TodoItem.objects.get(pk = item_id)
  # return HttpResponse("You are looking at {{item_id}}")
  return render(request, 'todo/detail.html', {'item':item})

class TodoItemList(generics.ListCreateAPIView):
  queryset = TodoItem.objects.all()
  serializer_class = TodoItemSerializer
  permission_classes = [
    permissions.AllowAny
  ]