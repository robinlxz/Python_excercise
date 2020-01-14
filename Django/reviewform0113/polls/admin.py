from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Snippet

class ChoiceInline(admin.TabularInline):
  model = Choice

class QuestionAdmin(admin.ModelAdmin):
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Snippet)