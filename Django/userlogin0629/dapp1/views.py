from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile

# Create your views here.


def index(request):
    all_users = UserProfile.objects.all()
    return HttpResponse(all_users)
