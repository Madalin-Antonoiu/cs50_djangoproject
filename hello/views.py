from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def mads(request):
    return HttpResponse("Hello, Mads!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")