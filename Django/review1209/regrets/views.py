from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View, generic
from rest_framework import generics

# Create your views here.
from .models import Behavior
from .serializers import BehaviorSerializer

def index(request):
  behavior_list = Behavior.objects.all()
  return render(request, 'regrets/index.html', {'behavior_list': behavior_list})


def behavior_api(request, behavior_id):
  behavior = Behavior.objects.get(pk=behavior_id)
  behavior.counts += 1
  behavior.save()
  return JsonResponse({
    "title":behavior.title,
    "text":behavior.text
  })

class Behavior_class(View):
  def get(self, request):
    return HttpResponse('result')

class BehaviorListCreateAPIView(generics.ListCreateAPIView):
  queryset = Behavior.objects.all()
  serializer_class = BehaviorSerializer

class IndexView(generic.ListView):
  model = Behavior
  template_name = 'regrets/index.html'