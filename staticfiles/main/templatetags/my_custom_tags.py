from django import template
from django.conf.urls.static import static
from main import views

register = template.Library()

@register.simple_tag
def chatbot():

    return ""