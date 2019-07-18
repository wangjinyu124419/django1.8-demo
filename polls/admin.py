# -*- coding: utf-8 -*-
import functools

from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from django.forms import MultipleChoiceField

from mysite.settings import logger
from .models import Question

#默认相对导入
from .models import Choice

# Register your models here.


class QuestionForm(forms.ModelForm):
    #flags对应model.py里PushRule类的flags
    #https://docs.djangoproject.com/en/1.8/ref/forms/fields/#multiplechoicefield
    #https://docs.djangoproject.com/en/1.8/ref/forms/widgets/#checkboxselectmultiple
    #https://docs.djangoproject.com/en/2.2/ref/forms/widgets/#widget
    #initial决定默认选中哪个
    flags = MultipleChoiceField(initial= ['1','4',], choices=[('1','Sound'),('2','Vibrate'),('4','Light'),])

    # logger.error('flags.widget:%s'%flags.widget)
    #ERROR:root:flags.widget:<django.forms.widgets.SelectMultiple object at 0x102679b90>
    # question_text = models.CharField(max_length=200)
    # date=models.DateField()

    # flags = MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'inline'}), initial='1|2|4', choices=[('1','Sound'),('2','Vibrate'),('4','Light')])
    # logger.error('flags.widget:%s'%flags.widget)
    #ERROR:root:flags.widget:<django.forms.widgets.CheckboxSelectMultiple object at 0x102679cd0>
    #is_stacked控制上下还是左右样式，label是左侧显示字样，Category123是选择框字样，required必要字段 choices是候选项
    # prefer_category = MultipleChoiceField(label='PreferCategory_label', required=False, widget=admin.widgets.FilteredSelectMultiple("Category123",is_stacked=False), initial=['1'],choices=[(c,c) for c in ['1','2']])
    # prefer_category = MultipleChoiceField(label='PreferCategory', required=False, choices=[(c,c) for c in ['1','2']])

    # logger.error('prefer_category:%s'%prefer_category.widget)

    # prefer_football = forms.CharField(label='FootballMatch', required=False, help_text='comma split match_ids')
    # prefer_football = forms.CharField(label='FootballMatch', required=False, widget=forms.TextInput(attrs={'style':'width:80%; margin-right:10px;'}), help_text='comma split match_ids')
    # logger.error('prefer_football.widget:%s'%prefer_football.widget)
    #ERROR:root:prefer_football.widget:<django.forms.widgets.TextInput object at 0x10a9b8dd0>
    class Meta:
        model = None
        # model = Question
        exclude = []

    logger.error('meta_mode:%s'%Meta.model)

    def __init__(self, *args, **kwargs):
        # logger.error('meta_mode:%s'%self.Meta.model)
        # logger.error('selflf.meta:%s'%self._meta)

        super(QuestionForm, self).__init__(*args, **kwargs)


        # self.initial['prefer_category'] = self.instance.news_tag.get('category',[])
        # self.initial['prefer_keyword']  = ','.join(self.instance.news_tag.get('keyword',[]))
        # self.initial['prefer_football'] = ','.join(self.instance.news_tag.get('football_match',[]))

    def clean(self):
        logger.error('self.cleaned_dat:%s'%self.cleaned_data)
        return self.cleaned_data

        # logger.error('self.instance is not None:%s'%self.instance)
        # logger.error('self.instance is not None:%s'%type(self.instance))
        #2019-06-21 11:04:39,274 ERROR [admin.py:271] -> self.instance:PushRule object

        # 这段self.initial['prefer_category']代码导致FilteredSelectMultiple的initia默认值不生效
        # self.initial['prefer_category'] = self.instance.news_tag.get('category',[])
        # self.initial['prefer_keyword']  = ','.join(self.instance.news_tag.get('keyword',[]))
        # self.initial['prefer_football'] = ','.join(self.instance.news_tag.get('football_match',[]))
        # logger.error('self.instance:%s'%self.instance)
        # logger.error('self.initial:%s'%self.initial)

    # def clean_flags(self):
    #     flags=self.cleaned_data.get('flags')
    #     if flags!=1:
    #         raise forms.ValidationError(u'failure', code='invalid')
    #     return flags
        # flags='test_flag'
        # return flags

# form = QuestionForm

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
    list_display_links = ('question_text',)
    actions = ['export_items_csv']
    actions_on_bottom=True
    list_per_page=10
    #显示其他对象，
    inlines = [ChoiceInline]
    # fieldsets控制添加数据是显示的字段

    #如果不注释这句代码，页面不显示actions，很奇怪
    show_full_result_count = False

    #单选按钮
    # radio_fields = {'year_in_school': admin.VERTICAL}


    fieldsets = [
        # ('target', {'fields': ['question_text','t','year_in_school','push_entire','flags','prefer_football']}),
        ('target', {'fields': ['question_text','t','year_in_school','push_entire','flags']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['pub_date'] }),
    ]
    # fieldsets[0][1]['fields'].remove('t')
    # exclude = ('t',)
    date_hierarchy='pub_date'
    # fields = ['question_text','pub_date']

    #如果指定了form，fieldsets一定要显示form中的一个字段？
    form = QuestionForm
    # if self.form.isva
    # if self.fo.is_valid():
    #     logger.error('self.clean_data:%s'%self.cleaned_data)
    # logger.error(form.Meta.model)
    # logger.error(type(form._meta))

    # def __init__(self,*args, **kwargs):
    #     super(QuestionAdmin, self).__init__(*args, **kwargs)
    #     logger.error('------%s'%self.model)


    # form.flags.widget
    def _x_news(self, obj):
        return '<a href="https://www.baidu.com/" target="_blank">wangjinyu</a>'


    _x_news.short_description ='short'

    # 允许html
    _x_news.allow_tags = True

    def export_items_csv(self, request, queryset):
        pass
    export_items_csv.short_description = "Export Selected as CSV"

    #重写get_urls方法
    #https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_urls
    def get_urls(self):
        # settings.LOG.error('invoke_get_urls')
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return functools.update_wrapper(wrapper, view)
        urls = super(QuestionAdmin, self).get_urls()
        # settings.LOG.info(urls)
        urlpatterns = [
            url(r'^addlist/$', wrap(self.add_view), name='news_af_pushrule_addlist'),
        ]
        return urlpatterns + urls

    # instance=None
    def save_form(self, request, form, change):
        logger.error('request:%s'%request)
        logger.error('request_address:%s'%id(request))

        # logger.error('save_form_form:%s'%form)
        # logger.error('save_form_change:%s'%change)
        logger.error('调用save_form')
        global  instance
        #add_list时的日志
        instance = super(QuestionAdmin, self).save_form(request, form, change)
        logger.error('instance:%s'%instance)
        logger.error('instance_address:%s'%id(instance))

        instance.t='test_save_form'
        #2019-06-22 03:36:55,745 DEBUG [admin.py:578] -> save_form_save_form:PushRule object
        #2019-06-22 03:36:55,745 DEBUG [admin.py:579] -> save_form_request:<QueryDict: {u'pushrulenode_set-1-url': [u'https://www.sunnewsonline.com/insecurity-south-east-govs-igp-meet-in-enugu/'], u'prefer_keyword': [u''], u'open_type': [u'transcoded'], u'product_version': [u''], u'pushrulenode_set-0-summary': [u''], u'pushrulenode_set-TOTAL_FORMS': [u'2'], u'pushrulenode_set-0-trans_url': [u'http://news.opera-api.com/news/detail/3e257568ddc933b0d9917d887a330b25'], u'pushrulenode_set-__prefix__-id': [u''], u'pushrulenode_set-1-country': [u'ng'], u'pushrulenode_set-1-entry_id': [u'32c79cf99d25d05a_ng'], u'pushrulenode_set-__prefix__-rule': [u''], u'pushrulenode_set-1-domain': [u'sunnewsonline.com'], u'pushrulenode_set-__prefix__-trans_url': [u''], u'pushrulenode_set-1-title': [u'Insecurity: South East govs, IGP meet in Enugu'], u'city': [u''], u'push_title': [u'push2'], u'pushrulenode_set-MIN_NUM_FORMS': [u'2'], u'pushrulenode_set-0-category': [u'News_Sports'], u'pushrulenode_set-1-rule': [u''], u'pushrulenode_set-1-push_icon': [u'http://img.transcoder.opera.com/assets/v1/7dbb3b96db5317bf67c48b5491266dbd?width=116&height=116'], u'pushrulenode_set-__prefix__-url': [u''], u'pushrulenode_set-__prefix__-push_icon': [u''], u'pushrulenode_set-0-push_icon': [u'http://img.transcoder.opera.com/assets/v1/3e257568ddc933b0d9917d887a330b25?width=116&height=116'], u'news_type': [u'normal'], u'pushrulenode_set-0-entry_id': [u'4927d9ca33bf196a_sl'], u'pushrulenode_set-0-domain': [u'goal.com'], u'pushrulenode_set-MAX_NUM_FORMS': [u'10'], u'pushrulenode_set-0-rule': [u''], u'test_mode': [u'0'], u'pushrulenode_set-1-summary': [u''], u'_save': [u''], u'pushrulenode_set-0-id': [u''], u'pushrulenode_set-1-category': [u'Others_Terrorism'], u'pushrulenode_set-__prefix__-country': [u''], u'soft_news': [u'no'], u'pushrulenode_set-1-language': [u'en'], u'pushrulenode_set-1-news_id': [u'7dbb3b96db5317bf67c48b5491266dbd'], u'pushrulenode_set-0-language': [u'en'], u'pushrulenode_set-__prefix__-category': [u''], u'pushrulenode_set-__prefix__-domain': [u''], u'csrfmiddlewaretoken': [u'LdayCOk2Odc6lGlG7WgQFdZybzGMsD5U'], u'pushrulenode_set-1-trans_url': [u'http://news-af.op-mobile.opera.com/news/detail/7dbb3b96db5317bf67c48b5491266dbd'], u'pushrulenode_set-__prefix__-title': [u''], u'pushrulenode_set-INITIAL_FORMS': [u'0'], u'prefer_football': [u''], u'pushrulenode_set-__prefix__-summary': [u''], u'push_type': [u'delay'], u'pushrulenode_set-0-news_id': [u'3e257568ddc933b0d9917d887a330b25'], u'pushrulenode_set-__prefix__-news_id': [u''], u'pushrulenode_set-__prefix__-entry_id': [u''], u'product_name': [u'all'], u'pushrulenode_set-0-title': [u'Argentina vs Paraguay Betting Tips: Latest odds, team news, preview and predictions'], u'pushrulenode_set-0-url': [u'https://www.goal.com/en-gb/news/argentina-vs-paraguay-betting-tips-latest-odds-team-news-preview-/15jkvj3znp4io1pth1q0u7c36c'], u'pushrulenode_set-__prefix__-language': [u''], u'flags': [u'1', u'2', u'4', u'8', u'16'], u'pushrulenode_set-0-country': [u'sl'], u'push_os': [u'all'], u'pushrulenode_set-1-id': [u'']}>

        return instance

    def save_model(self, request, obj, form, change):
        logger.error('request:%s'%request)
        logger.error('request_address:%s'%id(request))
        obj_test=obj
        global instance
        logger.error('调用save_model')
        logger.error('obj:%s'%obj)
        logger.error('obj_addressss:%s'%id(obj))
        logger.error('obj is install:%s'%(obj is instance))
        obj.save()
    #     #https://docs.djangoproject.com/en/1.8/ref/models/querysets/#update
    #     #TODO
    #     #deleted
    def get_inline_instances(self, request, obj=None):
        # self.inlines = []
        #如果是addlist
        # self.inlines=[ChoiceInline]
        return super(QuestionAdmin, self).get_inline_instances(request, obj=obj)
    # def save_form(self, request, form, change):
    #     logger.error('调用save_from')
    # def save_model(self, request, obj, form, change):
    #     logger.error('调用save_mode')
    #重写get_urls方法，自定义admin路由
    # def get_urls(self):
    #     urls = super(QuestionAdmin, self).get_urls()
    #     my_urls = [
    #         url(r'^myview/$', self.my_view),
    #     ]
    #     print my_urls + urls
    #     return my_urls + urls
    #
    # def my_view(self, request):
    #     # ...
    #     context = dict(
    #        # Include common variables for rendering the admin template.
    #        self.admin_site.each_context(request),
    #        # Anything else you want in the context...
    #        key='get_url',
    #     )
    #     return HttpResponse('override get url')
        # return TemplateResponse(request, "sometemplate.html", context)



class ChoiceAdmin(admin.ModelAdmin):
    #添加过滤筛选功能
    list_filter = ['votes','choice_text']

    #添加搜索框
    search_fields = ['votes']

    # 默认显示对象的__str__,list_display显示指定字段
    list_display = ('id','choice_text','_x_news','votes',)

    actions = ['export_items_csv']
    actions_on_bottom=True
    list_per_page=10
    #显示其他对象，

    # form = QuestionForm


    #如果不注释这句代码，页面不显示actions，很奇怪
    show_full_result_count = False

    #单选按钮
    # radio_fields = {'year_in_school': admin.VERTICAL}
    # fieldsets控制添加数据是显示的字段
    fieldsets = [
        ('target', {'fields': ['choice_text','question']}),
        ('Date information', {'fields': ['votes'], 'classes': ['collapse']}),
    ]
    # date_hierarchy='pub_date'
    # fields = ['question_text','pub_date']
    # logger.error('flags.widget:%s'%form.flags.widget)

    # form.flags.widget
    def _x_news(self, obj):
        return '<a href="https://www.baidu.com/" target="_blank">wangjinyu</a>'


    _x_news.short_description ='short'

    # 允许html
    _x_news.allow_tags = True

    def export_items_csv(self, request, queryset):
        pass
    export_items_csv.short_description = "Export Selected as CSV"


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
admin.site.register(Choice,ChoiceAdmin)
# admin.site.register(Choice)


