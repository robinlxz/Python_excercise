from django.urls import path
from . import views


app_name = 'dba'
urlpatterns = [
  path('', views.index),
  path('function_index', views.index, name='index'),
  path('view_index', views.IndexView.as_view(), name='view_index'),
  path('<int:event_id>/submit/', views.submit, name='submit'),
  path('event', views.event_form, name='event_form'),
]