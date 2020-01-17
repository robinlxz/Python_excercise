from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('questionform', views.question_and_input),
  path('question_detail/<int:question_id>/', views.question_detail, name='question_detail'),
  path('question_detail/<int:question_id>/result', views.question_result, name='result'),
  path('form/', views.contact),
  path('snippet/', views.snippet_detail),
]