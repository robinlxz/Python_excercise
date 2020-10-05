from django.urls import path
from . import views

app_name = 'event1210'

urlpatterns = [
  path('api/get_view/', views.MyView.as_view() ),
  path('', views.index, name='index'),
  path('api/all_question', views.all_question_api, name='all_question_api'),
]