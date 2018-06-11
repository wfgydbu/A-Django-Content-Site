from django import template

register = template.Library()

@register.filter
def title_tunc(value):
    length = 20
    if len(value) > length:
        return value[:length] + '...'
    else:
        return value