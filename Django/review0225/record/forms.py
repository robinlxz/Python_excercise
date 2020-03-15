from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
  class Meta:
    model = Person
    fields = ['name', 'age']

class PersonAgeForm(forms.ModelForm):
  class Meta:
    model = Person
    fields = ['age']