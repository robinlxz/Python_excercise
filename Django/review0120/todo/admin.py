from django.contrib import admin

# Register your models here.
from .models import Task, SubTask

class SubtaskInline(admin.TabularInline):
  model = SubTask
  extra = 1

class TaskAdmin(admin.ModelAdmin):
  inlines = [SubtaskInline]
  

admin.site.register(Task, TaskAdmin)