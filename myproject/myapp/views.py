from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def home(request): 

    return HttpResponse("Hello, Welcome to the Home Page!! ") 

def about(request):
    return HttpResponse("This is the About us page!!")
