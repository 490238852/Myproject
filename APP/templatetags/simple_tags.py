from django import template

register = template.Library()

@register.simple_tag
def my_simpletag(num1,num2):
    print('-----------   my  simpletag')
    return num1+num2