from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Question, Choice, User
from .forms import ChoiceForm

# Create your views here.

def index(request):
  question_list = Question.objects.all()
  context = {
    'question_list': question_list
  }
  return render(request, 'event0123/index.html', context)

#This function is not used, as I don't konw how to use question form to update choice value 20190126
def question_bet(request, question_id):
  question = Question.objects.get(pk=question_id)
  choices_for_question = Choice.objects.filter(question = question_id)
  context = {
    'question': question,
    'choices_for_question': choices_for_question
  }
  # return HttpResponse('bet page for question %s' %question_id)
  return render(request, 'event0123/question_bet.html', context)

def choice_bet(request, choice_id):
  choice = Choice.objects.get(pk=choice_id)
  previous_choice_bet = choice.choice_bet
  choice_form = ChoiceForm(request.POST, instance=choice)
  user = User.objects.get(pk=1)
  if choice_form.is_valid():
    choice_form.save()
    ### forms.attribute not works here
    # print(choice_form._meta.fields)
    # print(choice_form.choice_bet)
    error_message = 0
    if choice.question.question_lock == True:
      error_message = 'Bet failed! You have done bet for the question already.'
    elif choice.choice_bet < 0:
      error_message = 'Bet failed! Bet chips need to be positive.'
    elif user.user_chips < choice.choice_bet:
      error_message = 'Bet failed! Not enough chips.'

    if error_message:
      choice.choice_bet = previous_choice_bet
      choice.save()
      return render(request, 'event0123/choice_bet.html', {
        'choice': choice,
        'choice_form': choice_form,
        'error_message': error_message
      })
    else:
      user.user_chips -= choice.choice_bet
      user.save()
      print(choice.choice_bet)
      if choice.choice_bet !=0:
        # print('lock this question')
        question = choice.question
        question.question_lock = True
        question.save()

  context = {
    'choice': choice,
    'choice_form': choice_form
  }

  # Below return is test for succeed update
  return render(request, 'event0123/choice_bet.html', context)
  # Final return should go to info page with bet

def question_info(request, question_id):
  question = Question.objects.get(pk=question_id)
  choices_for_question = Choice.objects.filter(question = question_id)
  context = {
    'question': question,
    'choices_for_question': choices_for_question
  }
  return render(request, 'event0123/question_info.html', context)

def user_info(request, user_id):
  user = User.objects.get(pk=user_id)
  context = {
    'user': user
  }
  return render(request, 'event0123/user_info.html', context)
  # return HttpResponse('this is for %s' %user_id)