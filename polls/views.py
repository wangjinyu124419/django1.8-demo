# -*- coding: utf-8 -*-
import json

from django.core import urlresolvers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext as _

# Create your views here.
from django.utils.translation import ungettext
from django.template import loader
import logging
def index(request):
    logging.error('request.method:%s'%request.method)
    m=request.GET.get('m')
    d=request.GET.get('d')

    output = _('Today is %(month)s %(day)s.') % {'month': m, 'day': d}
    # return HttpResponse(output)output
    #重定向到admin后台
    # return HttpResponseRedirect( urlresolvers.reverse('admin:index') )
    # return HttpResponseRedirect()
    response = HttpResponse(json.dumps({"ajax": "cross"}))
    response["Access-Control-Allow-Origin"] = "http://localhost:8008"
    # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"

    #https://stackoverflow.com/questions/20478312/default-value-for-access-control-allow-methods/44385327#44385327
    response["Access-Control-Allow-Methods"] = "GET"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = "*"
    return response
    # template = loader.get_template('ajax_cors.html')
    # return HttpResponse(template.render())

    # return HttpResponseRedirect('http://www.baidu.com')
    # return HttpResponseRedirect('http://www.baidu.com')

    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request):
    question_id='1'
    question_id=int(question_id)
    page = ungettext(
        'there is %(count)d object',
        'there are %(count)d objects',
        question_id) % {
               'count': question_id,
           }
    return HttpResponse(page)
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)