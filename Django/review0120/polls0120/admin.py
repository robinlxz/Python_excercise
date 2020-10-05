from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
  model = Choice
  fields = ['choice_text', 'votes']
  extra = 1

class QuestionAdmin(admin.ModelAdmin):
  inlines = [ChoiceInline]
  



admin.site.register(Question, QuestionAdmin)