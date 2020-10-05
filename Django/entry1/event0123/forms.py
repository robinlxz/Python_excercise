from django import forms
from .models import Question, Choice

class ChoiceForm(forms.ModelForm):
  class Meta:
    model = Choice
    fields = ['choice_bet',]