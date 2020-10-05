from django import forms
from .models import NotdoItem

class NotdoItemForm(forms.ModelForm):
  class Meta:
    model = NotdoItem
    fields = ['notdo_name']

class NotdoItemDescForm(forms.ModelForm):
  class Meta:
    model = NotdoItem
    fields = ['notdo_description']    