from django.urls import path
from . import views

app_name = 'bet'

urlpatterns = [
  path('', views.IndexView.as_view(), name='index',)
]