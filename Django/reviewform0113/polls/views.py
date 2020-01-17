from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
from .models import Question, Choice
from .forms import ContactForm, SnippetForm, QuesitonForm

class IndexView(View):
    
  def get(self, request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
      'question_list':question_list,
    }
    return render(request, 'polls/index.html', context)

  def post(self, request):
    question_form = QuesitonForm()
  



def question_and_input(request):
  question_list = Question.objects.order_by('-pub_date')[:5]
  question_form = QuesitonForm()

  if request.method == 'POST':
    question_form = QuesitonForm(request.POST)
    if question_form.is_valid():
      question_form.save()

  context = {
    'question_list':question_list,
    'question_form':question_form,
  }
  
  return render(request, 'polls/index.html', context)

def question_detail(request, question_id):
  question = Question.objects.get(pk=question_id)
  return render(request, 'polls/detail.html', {'question':question})

def  question_result(request, question_id):
  question = Question.objects.get(pk=question_id)
  return render(request, 'polls/result.html', {'question':question})



  ## Below is for learning how to do post
def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['contact_name']
      email = form.cleaned_data['email']
      print(name, email)
  # return HttpResponse('Place holder: contact form.')
  # form = ContactForm()
  return render(request, 'polls/form.html', {'form':form})


def snippet_detail(request):

  form = SnippetForm()

  if request.method == 'POST':
    form = SnippetForm(request.POST)
    if form.is_valid():
      print("snippet is VALID")
      form.save()
  

  return render(request, 'polls/form.html', {'form':form})
