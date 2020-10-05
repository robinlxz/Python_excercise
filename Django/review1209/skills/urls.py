from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:skill_id>/', views.detail, name='detail'),
  path('api/', views.SkillListCreateAPIView.as_view() ),
  path('api/plus/<int:skill_id>/', views.skill_point_plusone, name='plus_one'),
  path('form/<int:skill_id>/', views.skill_update_with_form, name='update_with_form'),
]