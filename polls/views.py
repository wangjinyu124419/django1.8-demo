# -*- coding: utf-8 -*-
import json
import time

from django.core import urlresolvers
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

# Create your views here.
from django.utils.translation import ungettext
from django.template import loader, Context
import logging

from .models import Question, Choice


def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
        'd': {'a':1},
        'l':[1,1,2],
        's':'wang111jinyu',
        # 'a' :mark_safe('<a href="http://www.cnblogs.com/0bug/">屠龙宝刀，点击就送</a>'),
        'a' : '<a href="http://www.cnblogs.com/0bug/">屠龙宝刀，点击就送</a>',
        # 'greeting':'<b>Hello!</b>',
        'greeting':'',
               }
    #
    # # context = {'django': 'the web framework for perfectionists with deadlines'}
    # return render(request, 'polls/index.html', context)
    # return render(request, 'father.html')
    return render(request, 'son.html',context)

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #
    # template = loader.get_template('polls/index.html')
    # context = {
    #     # 'latest_question_list': latest_question_list,
    #     'wang':'wangjinyu'
    # }
    # return HttpResponse(template.render(context, request))



    # time.sleep(5)
    # logging.error('request.method:%s'%request.method)
    # m=request.GET.get('m')
    # d=request.GET.get('d')

    # output = _('Today is %(month)s %(day)s.') % {'month': m, 'day': d}
    # return HttpResponse(output)output
    #重定向到admin后台
    # return HttpResponseRedirect( urlresolvers.reverse('admin:index') )
    # return HttpResponseRedirect()
    # response = HttpResponse(json.dumps({"ajax": "cross"}))
    # response["Access-Control-Allow-Origin"] = "http://localhost:8008"
    # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"

    #https://stackoverflow.com/questions/20478312/default-value-for-access-control-allow-methods/44385327#44385327
    # response["Access-Control-Allow-Methods"] = "GET"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = "*"
    # return response
    # template = loader.get_template('ajax_cors.html')
    # return HttpResponse(template.render())

    # return HttpResponseRedirect('http://www.baidu.com')
    # return HttpResponseRedirect('http://www.baidu.com')

    # return HttpResponse("Hello, world. You're at the polls index.")

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    # question_id='1'
    #     # question_id=int(question_id)
    #     # page = ungettext(
    #     #     'there is %(count)d object',
    #     #     'there are %(count)d objects',
    #     #     question_id) % {
    #     #            'count': question_id,
    #     #        }
    #     # return HttpResponse(page)
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
# def results(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
    # return HttpResponse(response)


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        id=request.POST['choice']
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        # return HttpResponseRedirect(reverse('polls:results', args=(10,)))
        # return HttpResponseRedirect(reverse('polls:results'))
