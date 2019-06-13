# -*- coding: utf-8 -*-
from django.contrib import admin

# from polls.models import Question
from .models import Question

#默认相对导入
from .models import Choice

# Register your models here.

#层级显示关联对象
# class ChoiceInline(admin.StackedInline):
#表格模式显示关联对象
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    #添加过滤筛选功能
    list_filter = ['pub_date']

    #添加搜索框
    search_fields = ['question_text']

    #默认显示对象的__str__,list_display显示指定字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    #显示其他对象
    inlines = [ChoiceInline]
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # fields = ['question_text','pub_date']

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
admin.site.register(Choice)