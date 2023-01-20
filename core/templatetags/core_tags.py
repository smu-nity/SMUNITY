from django import template

register = template.Library()


@register.filter
def sub(a, b):
    if not b:
        b = 0
    if b >= a:
        return 0
    return a - b


@register.filter
def div(a, b):
    if not a:
        a = 0
    if a >= b:
        return 100
    return int(a / b * 100)


@register.filter
def zero_filter(a):
    if a:
        return a
    return 0
