from django.urls import path
from .views import ItemListCreate
from . import views

urlpatterns = [
  path('api/item/', views.ItemListCreate.as_view() )
]