from django import template
register = template.Library()

@register.filter
def get_len(element):
    print(element)
    for i in element:
        len_element = (len(element[i]))
        break
    result = []
    for i in range(len_element):
        result.append(i) 
    return result