from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse

# Create your views here.
from .models import Question, Choice
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
  question_list = Question.objects.all()
  question_form = QuestionForm()
  if request.method == 'POST':
    question_form = QuestionForm(request.POST)
    if question_form.is_valid():
      question_form.save()
      print('saved %s' %question_form)

  context = {
    'question_list': question_list,
    'question_form': question_form
  }
  return render(request, 'polls/index.html', context)


def details(request, question_id):
  question = Question.objects.get(pk=question_id)
  context = {
    'question': question
  }
  return render(request, 'polls/details.html', context)

def vote_page(request, question_id):
  question = Question.objects.get(pk=question_id)
  context = {
    'question': question
  }
  return render(request, 'polls/vote_page.html', context)


def vote(request, question_id, choice_id):
  choice = Choice.objects.get(pk=choice_id)
  choice.votes += 1
  choice.save()
  # return HttpResponse('Vote for question %s choice %s is done' %(question_id,choice_id))
  # return HttpResponseRedirect(reverse('polls:index'))
  return HttpResponseRedirect(reverse('polls:details', args=(question_id,)))