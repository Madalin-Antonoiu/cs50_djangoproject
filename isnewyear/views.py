from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()

    return render(request, "isnewyear/index.html", {
        "newyear": now.month == 1 and now.day == 1 # If first month and first day ( 1st Jan) this will return true
    })