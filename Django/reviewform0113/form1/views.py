from django.shortcuts import render

# Create your views here.
from .forms import ContactForm

def contact(request):

  # return render(request, 'form1/index.html', {'form':form})
  # form = ContactForm(request.POST)

  if request.method == 'POST':    
    form = ContactForm(request.POST)
    # print(type(form.cleaned_data))
    if form.is_valid(): #Call this method add an attribute as dict to the class
      print(type(form.is_valid()))
      print(type(form.cleaned_data))
      name = form.cleaned_data['name']
      region = form.cleaned_data['region']
      print(name, region)
  
  return render(request, 'form1/index.html', {'form':form})