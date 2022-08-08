from django import template

register = template.Library()

def cut(value,arg):
    '''
    THIS CUTS OUT ALL VALUE OF STRING
    '''

    return value.replace(arg,'')

register.filter('cut', cut)    
