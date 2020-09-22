from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello, World")
    return render(request, "hello/index.html")

def mads(request):
    return HttpResponse("Hello, Mads!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}")
    context = {
         "name": name.capitalize()
    }
    
    return render(request, "hello/greet.html", context)