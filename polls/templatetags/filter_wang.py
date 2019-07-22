import datetime

from django import template
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()

@register.filter(name='filter_name')
def filter_test(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, 'filter')

# register.filter('filter_name', filter_test)

@register.simple_tag(takes_context=True, name='simpletag')
# def current_time(context,format_string):
def current_time(context,a,b,*args,**kwargs):
    # context=context['TIME_ZONE']
    args=args
    return a+b+args[0]+args[1]+kwargs['e']
    # return format_string[:10]