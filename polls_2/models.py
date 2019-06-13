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

    #指定排序字段
    was_published_recently.admin_order_field = 'pub_date'

    #True会显示✅，False显示原始值
    was_published_recently.boolean = True

    #字段简称
    was_published_recently.short_description = 'Published recently?'

    #魔法方法
    def __str__(self):
        return self.question_text

    # class Meta:
    #     app_label = 'polls_2'  # 定义该model的app_label



class Choice(models.Model):
    #外键
    question = models.ForeignKey(Question)
    #wangjinyu_choice是choice_text的别名
    choice_text = models.CharField('wangjinyu_choice',max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    # class Meta:
    #     app_label = 'polls_2'  # 定义该model的app_label

