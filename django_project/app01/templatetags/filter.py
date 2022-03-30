from django.template.library import Library
from datetime import date

register = Library()


@register.filter
def add_str(str1, str2):
    return str1 + str2


@register.filter
def turn_date(date_time):
    return date_time.strftime('%Y-%m-%d')


@register.simple_tag
def t_date(date_time):
    return date_time.strftime('%Y-%m-%d')


