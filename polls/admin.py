# -*- coding: utf-8 -*-
from django.contrib import admin

from polls.models import Question
# from .models import Question

#默认相对导入
from .models import Choice

# Register your models here.


admin.site.register(Question)
admin.site.register(Choice)