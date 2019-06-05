from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')

def faq(request):
    return render(request, 'pages/faq.html')

def termsofuse(request):
    return render(request, 'pages/termsofuse.html')

def privacypolicy(request):
    return render(request, 'pages/privacypolicy.html')

def contact(request):
    return render(request, 'pages/contactus.html')

