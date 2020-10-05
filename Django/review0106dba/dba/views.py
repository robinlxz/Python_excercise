from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Event, Duty, SubDuty
from django.views import View

def index(request):
  all_event = Event.objects.all()
  all_duty = Duty.objects.all()
  form = EventForm()
  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      print('event form submitted')
      form.save()
  index_dict = {
    'all_event': all_event,
    'all_duty': all_duty,
    'form':form
  }
  return render(request, 'dba/index.html', index_dict)


class IndexView(View):
  def get(self, request, *args, **kwargs):
    all_event = Event.objects.all()
    all_duty = Duty.objects.all()
    index_dict = {
      'all_event': all_event,
      'all_duty': all_duty
    }
    return render(request, 'dba/index.html', index_dict)


# def submit(request):
#   selected_duty = Duty.objects.get(pk=1)
#   selected_duty.count += 1
#   selected_duty.save()
#   return HttpResponse(selected_duty.count)

def submit(request, event_id):
  selected_event = Event.objects.get(pk=event_id)
  selected_event.event_count += 1
  selected_event.save()
  return HttpResponse(selected_event.event_count)



from .forms import EventForm

def event_form(request):
  form = EventForm()
  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      print('2nd event form submitted')
      form.save()
  context = {
    'form':form
  }
  return render(request, 'dba/event_form.html', context)
