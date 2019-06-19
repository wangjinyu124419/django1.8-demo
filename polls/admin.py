# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

# from polls.models import Question
from django.http import HttpResponse
from django.template.response import TemplateResponse

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
    list_filter = ['pub_date','question_text']

    #添加搜索框
    search_fields = ['question_text']

    #默认显示对象的__str__,list_display显示指定字段
    list_display = ('_x_news','question_text','t', 'pub_date', 'was_published_recently',)

    actions = ['export_items_csv']
    actions_on_bottom=True
    list_per_page=1
    #显示其他对象，
    inlines = [ChoiceInline]
    # fieldsets控制添加数据是显示的字段

    #如果不注释这句代码，页面不显示actions，很奇怪
    show_full_result_count = False

    fieldsets = [
        ('target', {'fields': ['question_text','t','year_in_school','push_entire']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # date_hierarchy='pub_date'
    # fields = ['question_text','pub_date']

    def _x_news(self, obj):
        return '<a href="https://www.baidu.com/" target="_blank">wangjinyu</a>'


    _x_news.short_description ='short'

    # 允许html
    _x_news.allow_tags = True

    def export_items_csv(self, request, queryset):
        pass
    export_items_csv.short_description = "Export Selected as CSV"

    #重写get_urls方法，自定义admin路由
    def get_urls(self):
        urls = super(QuestionAdmin, self).get_urls()
        my_urls = [
            url(r'^myview/$', self.my_view),
        ]
        print my_urls + urls
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           # Anything else you want in the context...
           key='get_url',
        )
        return HttpResponse('override get url')
        # return TemplateResponse(request, "sometemplate.html", context)

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
admin.site.register(Choice)