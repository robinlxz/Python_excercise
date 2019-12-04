from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializer import ItemSerializer
from .models import Item

class ItemList(generics.ListCreateAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer