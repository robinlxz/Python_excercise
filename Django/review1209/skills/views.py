from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Skill
from rest_framework import generics, permissions
from .serializers import SkillSerializer
from .forms import SkillForm
from django.urls import reverse

def index(request):
  # return HttpResponse('This is skill index page.')
  skill_list = Skill.objects.all()
  skill_form = SkillForm()
  if request.method == "POST":
    skill_form = SkillForm(request.POST)
    if skill_form.is_valid():
      skill_form.save()
  context = {
    'skill_list':skill_list,
    'skill_form':skill_form
    }
  return render(request, 'skills/index.html', context)

def detail(request, skill_id):
  skill = Skill.objects.get(pk = skill_id)
  return render(request, 'skills/detail.html', {'skill':skill}) 

def skill_point_plusone(request, skill_id):
  skill = Skill.objects.get(pk = skill_id)
  skill.skill_point += 1
  skill.save()
  # return HttpResponse('added')
  return HttpResponseRedirect(reverse('skills:detail', args=(skill.id,)))

class SkillListCreateAPIView(generics.ListCreateAPIView):
  queryset = Skill.objects.all()
  serializer_class = SkillSerializer
  permission_classes = [
    permissions.AllowAny
  ]

# Test for update existing model with forms: https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/

def skill_update_with_form(request, skill_id):
  skill = Skill.objects.get(pk = skill_id)
  form = SkillForm(instance=skill)
  skill.skill_point -= 1
  skill.save()
  # print(request.POST) #not working
  # if form.is_valid():
  #   skill.skill_point = form.skill_point
  #   skill.save()
  return HttpResponseRedirect(reverse('skills:detail', args=(skill.id,)))
