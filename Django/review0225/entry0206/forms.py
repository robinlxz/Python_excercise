from .models import Question, Choice
from django import forms


class ChoiceForm(forms.ModelForm):
  class Meta:
    model = Choice
    fields = ['choice_chips', ]
    
