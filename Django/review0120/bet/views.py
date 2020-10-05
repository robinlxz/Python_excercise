from django.shortcuts import render
from django.views import View
from .models import Team
from .forms import TeamForm

# Create your views here.
class IndexView(View):

  def get(self, request):
    team1 = Team.objects.get(pk=3)
    team_list = Team.objects.all()
    form = TeamForm()
    context = {
      'team1': team1,
      'form': form,
      'team_list': team_list
    }
    return render(request, 'bet/index.html', context)

  def post(self, request):
    team1 = Team.objects.get(pk=3)
    team_list = Team.objects.all()
    form = TeamForm(request.POST, instance=team1)
    if form.is_valid():
      print('valid!')
      form.save()
    context = {
      'team1': team1,
      'form': form,
      'team_list': team_list
    }
    return render(request, 'bet/index.html', context)