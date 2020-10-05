from django.urls import path
from . import views

app_name = 'lxzapi'

urlpatterns = [
  path('', views.index, name='index'),
  path('api/choice/<int:choice_id>', views.choice_lxz_api),
  path('api/api_bet_on_choice_one/<int:bet_amount>', views.api_bet_on_choice_one),
  path('api/A_bet_on_specific_choice/<int:choice_id>/<int:bet_amount>', views.A_bet_on_specific_choice),
]