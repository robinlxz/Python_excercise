from django.shortcuts import render
from .models import NotdoItem
# below is for API
from rest_framework import generics
from .serializer import NotdoItemSerializer
# below is for form
from .forms import NotdoItemForm, NotdoItemDescForm


# Create your views here.
def index(request):
  notdo_item_list = NotdoItem.objects.all()
  notdo_item_form = NotdoItemForm()
  if request.method == "POST":
    notdo_item_form = NotdoItemForm(request.POST)
    if notdo_item_form.is_valid():
      print("notdo_item_form is valid")
      notdo_item_form.save()

  context = {
    'notdo_item_list':notdo_item_list,
    'notdo_item_form':notdo_item_form
  }
  return render(request, 'notdolist/index.html', 
  context)


def detail(request, item_id):
  # Should do "try-except"
  notdo_item = NotdoItem.objects.get(pk=item_id)
  notdo_item_desc_form = NotdoItemDescForm()
  if request.method == "POST":
    notdo_item_desc_form = NotdoItemDescForm(request.POST)
    notdo_item_desc_form.save()
  context = {
    'notdo_item': notdo_item,
    'notdo_item_desc_form': notdo_item_desc_form
  }
  return render(request, 'notdolist/detail.html', context)

class NotdoItemList(generics.ListCreateAPIView):
  queryset = NotdoItem.objects.all()
  serializer_class = NotdoItemSerializer