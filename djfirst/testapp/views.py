from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greetings(request):
    s="<h1>this is my first view</h1>"
    return HttpResponse(s)