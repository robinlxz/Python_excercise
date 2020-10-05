from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Question, Choice

# Create your views here.

class MyView(View):
  def get(self, request):
    return HttpResponse('result for get function in View class')

  # POST does not work this way, due to CSRF error 
  # def post(self, request):
  #   return HttpResponse('result for post function in View class')

def index(request):
  question_list = Question.objects.all()
  return render(request, 'event1210/index.html', {'question_list':question_list})  


def all_question_api(request):
  question_list = Question.objects.all()
  # all_question_json = {"test_json":question_list}
  all_question_json = {"test_json":'abcd'}
  # return HttpResponse(question_list)
  return JsonResponse(all_question_json)