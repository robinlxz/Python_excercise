from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:question_id>', views.details, name='details'),
  path('<int:question_id>/vote_page', views.vote_page, name='vote_page'),
  path('<int:question_id>/<int:choice_id>/vote_action', views.vote, name='vote'),
]