from django import template
register = template.Library()

@register.filter
def get_to_int(element):
    try:
        result = int(element)
        return result
    except:
        return element
