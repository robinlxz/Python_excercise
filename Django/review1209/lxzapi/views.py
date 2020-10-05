from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Choice
from django.http import JsonResponse


def index(request):
  choice_list = Choice.objects.all()
  return render(request, 'lxzapi/index.html', {'choice_list':choice_list})

def choice_lxz_api(request, choice_id):
  choice = Choice.objects.get(pk=choice_id)
  result_json = {
    "choice_text": choice.choice_text,
    "teamA_bet": choice.teamA_bet,
    "teamB_bet": choice.teamB_bet
  }
  return JsonResponse(result_json)

def api_bet_on_choice_one(request, bet_amount):
  choice = Choice.objects.get(pk=1)
  choice.teamA_bet += bet_amount
  choice.save()
  return HttpResponse("Added!")

def A_bet_on_specific_choice(request, choice_id, bet_amount):
  try:
    choice = Choice.objects.get(pk=choice_id)
  except:
    raise "Choice not exist!"
  choice.teamA_bet += bet_amount
  choice.save()
  return HttpResponse("Added!")