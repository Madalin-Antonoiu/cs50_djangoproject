from django import forms
from django.http import HttpResponse
from django.shortcuts import render

tasks = ["Do groceries", "Buy some soap", "Clean the dishes"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
def add(request):
    if request.method == "POST":
        return render(request, "tasks/index.html")
        # Grab the data and do things with it
    else:
        return render(request, "tasks/add.html", {
            "form": NewTaskForm()
        })