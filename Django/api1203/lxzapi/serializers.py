from rest_framework import serializers
from lxzapi.models import Lead

class LeadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lead
    fields = ('id', 'name', 'email')