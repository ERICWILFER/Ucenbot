from django.http import HttpResponse
from django.shortcuts import render

from .forms import FeedbackForm

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


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'form/thanks.html')
    else:
        form = FeedbackForm()
    context = {'form' : form}
    return render(request, 'form/feedback_form.html', {'form': form})