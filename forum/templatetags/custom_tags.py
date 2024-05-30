from django import template

register = template.Library()


@register.filter(name="endswith")
def endswith(value, arg):
    return value.lower().endswith(arg.lower())


@register.filter(name="last_of")
def last_of(value, arg):
    return value[arg]
