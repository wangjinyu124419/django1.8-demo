# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.utils import timezone


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    #自定义方法
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    #魔法方法
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField('wangjinyu_choice',max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

