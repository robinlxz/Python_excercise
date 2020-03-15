from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views import View
from .models import Question, Choice, User
from .forms import ChoiceForm

class IndexView(View):
  def get(self, request):
    all_questions = Question.objects.all()
    context = {
      'all_questions': all_questions,
    }
    return render(request, 'entry0206/index.html', context)


def question_info(request, question_id):
  all_question_choices = Choice.objects.filter(question=question_id)
  context = {
    'all_question_choices' : all_question_choices,
  }
  print('question id is', question_id)
  print(all_question_choices)
  return render(request, 'entry0206/question_info.html', context)

def question_bet(request, question_id):
  question = Question.objects.get(pk=question_id)
  all_choices_from_question = Choice.objects.filter(question=question_id)
  # print(all_choices_from_question)
  all_choice_forms = []
  for choice in all_choices_from_question:
    all_choice_forms.append(ChoiceForm(instance=choice))
    # print(choice.id)
  # print(type(all_choice_forms))

  context = {
    'question': question,
    'all_choices_from_question': all_choices_from_question,
    'all_choice_forms': all_choice_forms
  }
  # return HttpResponse('Question Bet page')
  return render(request, 'entry0206/question_bet.html', context)