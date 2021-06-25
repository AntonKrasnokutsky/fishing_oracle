from django import template
register = template.Library()

@register.filter
def get_element(elements, key):
    return elements[key]