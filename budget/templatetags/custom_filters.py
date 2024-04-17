from django import template

register=template.Library()

@register.filter
def calculate_percentage(value,total):

    return 0 if total==0 else (value/total)*100