from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(max_length=100, label='Contact Name')
  region = forms.ChoiceField(choices=[('sg','Singapore'), ('cn', 'China')])