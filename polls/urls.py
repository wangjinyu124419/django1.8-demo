from django.conf.urls import url

from . import views

urlpatterns = [
    #ex:/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/any
    # url(r'^(?P<question_id>[0-9]+)', views.detail, name='detail'),
    # ex: /polls/5/
    url('^(?P<question_id>[0-9]+)$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]