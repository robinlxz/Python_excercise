from django.urls import path
from . import views

app_name = 'regrets'

urlpatterns = [
  path('', views.index, name='index'),
  path('api/behavior/<int:behavior_id>/', views.behavior_api),
  path('api/behavior_list/', views.BehaviorListCreateAPIView.as_view() ),
]