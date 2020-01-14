from django import forms
from .models import Snippet, Question

class ContactForm(forms.Form):
  contact_name = forms.CharField(label='Contact Name', max_length=100)
  email = forms.EmailField(label='E-mail')
  category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
  subject = forms.ChoiceField(required=False)
  body = forms.CharField(widget=forms.Textarea)


class SnippetForm(forms.ModelForm):

  class Meta:
    model = Snippet
    fields = ('name', 'body')


class QuesitonForm(forms.ModelForm):

  class Meta:
    model = Question
    fields = ('question_text',)