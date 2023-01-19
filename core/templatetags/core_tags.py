from django import template

register = template.Library()


@register.filter
def sub(a, b):
    if b >= a:
        return 0
    return a - b

@register.filter
def div(a, b):
    if a >= b:
        return 100
    return int(a / b * 100)
