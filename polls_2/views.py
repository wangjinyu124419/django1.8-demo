# -*- coding: utf-8 -*-
from django.core import urlresolvers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def index(request):

    #重定向到admin后台
    return HttpResponseRedirect( urlresolvers.reverse('admin:index') )
    # return HttpResponseRedirect( urlresolvers.reverse('admin:index'.format()) )

    # return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)