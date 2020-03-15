from django.shortcuts import render, HttpResponse
from .models import Person, Symptom
from .forms import PersonForm, PersonAgeForm

# Create your views here.
def index(request):
  all_people = Person.objects.all()
  person_form = PersonForm()
  if request.method == 'POST':
    print("method is POST")
    person_form = PersonForm(request.POST)
    if person_form.is_valid():
      print("valid")
      person_form.save()
    else:
      print("hmm, invalid")
  else:
    print("method is not POST")
  context = {
    'all_people' : all_people,
    'person_form' : person_form
  }
  return render(request, 'record/index.html', context)


def update_age(request, person_id):
  person = Person.objects.get(pk=person_id)
  person_age_form = PersonAgeForm(request.POST, instance=person)
  if request.method == 'POST':
    if person_age_form.is_valid():
      person_age_form.save()
  context = {
    'person': person,
    'person_age_form': person_age_form
  }
  return render(request, 'record/update_age.html', context)