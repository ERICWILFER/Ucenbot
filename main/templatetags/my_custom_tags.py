from django import template

register = template.Library()


@register.simple_tag
def chatbot():
    num1 = int(input("enter the first number"))
    num2 = int(input("enter the second number"))

# Adding two nos
    sum = num1 + num2

# printing values
    return("Sum of {0} and {1} is {2}" .format(num1, num2, sum))
