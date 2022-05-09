from django import template
from django.conf.urls.static import static


register = template.Library()

@register.simple_tag
def chatbot():
    
    print("success")