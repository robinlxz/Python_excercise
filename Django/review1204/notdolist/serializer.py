from rest_framework import serializers
from .models import NotdoItem

class NotdoItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = NotdoItem
    fields = ['id', 'notdo_name', 'notdo_description', 'start_time']