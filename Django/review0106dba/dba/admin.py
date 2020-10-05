from django.contrib import admin

# Register your models here.
from .models import Event, Duty, SubDuty

# admin.site.register(Event)
# admin.site.register(Duty)
# admin.site.register(SubDuty)


class SubDutyInline(admin.TabularInline):
  model = SubDuty
  extra = 2

class DutyAdmin(admin.ModelAdmin):
  inlines = [SubDutyInline]


admin.site.register(Event)
admin.site.register(Duty, DutyAdmin)  