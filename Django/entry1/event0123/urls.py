from django.urls import path
from . import views

app_name = 'event0123'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:question_id>/bet', views.question_bet, name='question_bet'),
  path('choice/<int:choice_id>/bet', views.choice_bet, name='choice_bet'),
  path('<int:question_id>/info', views.question_info, name='question_info'),
  path('user/<int:user_id>/', views.user_info, name='user_info'), #There must be "/" at the end
]