# creating custom filters
from django import template

register = template.Library()

@register.filter(name='cutt') # decorators are used here to register this custom filter
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """

    return value.replace(arg, '')


#register.filter('cut', cut) # here the 'cut' is the name of the custom filter
