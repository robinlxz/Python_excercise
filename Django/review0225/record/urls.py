from django.urls import path
from . import views

app_name = 'record'

urlpatterns = [
  path('', views.index, name='index'),
  path('update_age/<int:person_id>', views.update_age, name='update_age'),
  path('api', views.fake_api, name='fake_api'),
]