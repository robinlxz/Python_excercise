from django.urls import path
from . import views

app_name = 'entry0206'

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('info/<int:question_id>', views.question_info, name='question_info'),
  path('bet/<int:question_id>', views.question_bet, name='question_bet'),
]