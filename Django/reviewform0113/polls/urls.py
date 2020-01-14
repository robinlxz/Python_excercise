from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('questionform', views.question_and_input),
  path('form/', views.contact),
  path('snippet/', views.snippet_detail),
]