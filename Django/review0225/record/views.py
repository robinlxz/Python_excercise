from django.shortcuts import render, HttpResponse
from .models import Person, Symptom
from .forms import PersonForm, PersonAgeForm
from django.http import JsonResponse

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

def fake_api(request):
  fake_return = {
      "events": [
        {
          "id": 1,
          "title": "Beach Cleanup",
          "date": "Aug 28 2018",
          "time": "10:00",
          "location": "Daytona Beach",
          "description": "Let's clean up this beach.",
          "organizer": "Adam Jahr",
          "category": "sustainability",
          "attendees": [
            {
              "id": "abc123",
              "name": "Adam Jahr"
            },
            {
              "id": "def456",
              "name": "Gregg Pollack"
            },
            {
              "id": "ghi789",
              "name": "Beth Swanson"
            },
            {
              "id": "jkl101",
              "name": "Mary Gordon"
            }
          ]
        },
        {
          "id": 2,
          "title": "Park Cleanup",
          "date": "Nov 12 2018",
          "time": "12:00",
          "location": "132 N Magnolia Street, Orlando, Florida",
          "description": "We're going to clean up this park.",
          "organizer": "Adam Jahr",
          "category": "nature",
          "attendees": [
            {
              "id": "ghi789",
              "name": "Beth Swanson"
            },
            {
              "id": "jkl101",
              "name": "Mary Gordon"
            }
          ]
        },
        {
          "id": 3,
          "title": "Pet Adoption Day",
          "date": "Dec 2 2018",
          "time": "12:00",
          "location": "132 N Magnolia Street, Orlando, Florida",
          "description": "Help animals find new homes.",
          "organizer": "Gregg Pollack",
          "category": "animal welfare",
          "attendees": [
            {
              "id": "abc123",
              "name": "Adam Jahr"
            },
            {
              "id": "ghi789",
              "name": "Beth Swanson"
            },
            {
              "id": "jkl101",
              "name": "Mary Gordon"
            }
          ]
        }
      ]
    }
  return JsonResponse(fake_return)