from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html")

def services(request):
    context = {}
    return render(request, "services.html")

def about(request):
    context = {}
    return render(request, "about.html")

def contact(request):
    context = {}
    return render(request, "contact.html")