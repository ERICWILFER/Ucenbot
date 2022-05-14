from django.http import HttpResponse
from django.shortcuts import render
from .forms import FeedbackForm
from . import canteenbot, sssbot

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
    context = {}
    return render(request, "gallery.html")


def canteen(request):
    context = {}

    def chat(msg):
        # print("Start chatting with the bot (type quit to stop)!")
        rresponse, contextimg = canteenbot.response(msg) 
        return rresponse

    def img():
        rresponse, contextimg = canteenbot.response(msg)
        return contextimg
        
    if request.method == 'POST':
        msg = request.POST.get('input', '')
        context['chatresponse'] = chat(msg)
        context['imgresponse'] = img()
        # return HttpResponse(chatresponse, content_type='text/plain')
    return render(request, "canteenbot.html",context)

def sss(request):
    context = {}

    def chat(msg):
        # print("Start chatting with the bot (type quit to stop)!")
        rresponse = sssbot.response(msg) 
        return rresponse
        
    if request.method == 'POST':
        msg = request.POST.get('input', '')
        context['chatresponse'] = chat(msg)


        # return HttpResponse(chatresponse, content_type='text/plain')
    return render(request, "sssbot.html",context)


def feedback_form(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'form/thanks.html')
    else:
        form = FeedbackForm()
    context = {'form': form}
    return render(request, 'form/feedback_form.html', {'form': form})


def chatbot(request):
    if request.method == 'POST':
        msg = request.POST.get('input', '')
        if msg == 'eric':
            return HttpResponse("eric is alive")
        else:
            return HttpResponse("eric is not alive")
    return render(request, 'chatbot.html')
