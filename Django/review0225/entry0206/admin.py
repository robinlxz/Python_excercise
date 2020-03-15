from django.contrib import admin

# Register your models here.
from .models import Question, Choice, User

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(User)



class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 1

class QuestionAdmin(admin.ModelAdmin):
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)