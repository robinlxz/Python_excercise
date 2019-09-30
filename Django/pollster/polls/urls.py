from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    #'''below one not figure out how to do yet lxz0930
    # path('<int:question_id>/detail/', views.detail, name='detail'),
    #'''
    # path('<int:question_id>/results/', views.results, name='results'), 
    path('<int:question_id>/resultssss/', views.results, name='result'),
    # What if the name='results' changed? where else should I change to make the link work again? Made: it's defined in index.html href, it go here based on the href="{% url 'polls:result' question.id %}"
    path('<int:question_id>/vote/', views.vote, name='vote'),
]