from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Item
from .serializer import ItemSerializer


class ItemListCreate(generics.ListCreateAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer