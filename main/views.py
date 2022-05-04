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
        msg = request.POST.get('input','')
        if msg == 'eric':
            return HttpResponse("eric is alive")
        else:
            return HttpResponse("eric is not alive")
    return render(request, 'chatbot.html')
    
    
    