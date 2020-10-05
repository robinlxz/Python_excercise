from django.contrib import admin
from .models import Team, Choice, Question


# Register your models here.


class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 0

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields':['question_text']}),
    ('Info', {'fields':['question_info']}),
  ]
  inlines = [ChoiceInline]


# admin.site.register(Team)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

