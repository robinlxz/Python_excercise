from django.contrib import admin

# Register your models here.
from .models import Question, Choice, User

class ChoiceInline(admin.TabularInline):
  model = Choice
  fields = ['choice_text', 'choice_odd', 'choice_bet']
  extra = 1

class QuestionAdmin(admin.ModelAdmin):
  inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(User)