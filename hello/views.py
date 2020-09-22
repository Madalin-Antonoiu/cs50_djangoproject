from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("Hello")

def mads(request):
    return HttpResponse("Hello, Mads!")

def greet(request, name):
    return HttpResponse(f"Hello, {name}")