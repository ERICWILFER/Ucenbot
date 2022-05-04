from django.http import HttpResponse
from django.shortcuts import render
from .forms import FeedbackForm, InputCreateView

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

def gallery(request):
    context ={}
    return render(request, "gallery.html")

def pythonweb(request):
    context ={}
    return render(request, "pythonweb.html")

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

def chatbot(request):
    if request.method == 'POST':
        form = InputCreateView(request.POST)
        # msg = request.POST.get('input')
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>ok</h1>')
    else:
        form = InputCreateView()
    context = {'form' : form}
    return render(request, 'chatbot.html', {'form': form})