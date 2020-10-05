from django.urls import path
from . import views

app_name = 'notdolist'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:item_id>', views.detail, name='detail'),
  path('api/notdoitem/', views.NotdoItemList.as_view() ),
]