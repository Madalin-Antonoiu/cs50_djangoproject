from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # Client side FORM validation - for free!
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":

        # Server side FORM validation - for free!
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # The valid, clean data is found in this form.cleaned_data var
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            
            return redirect("tasks:index")
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
            # Actualy send back the same form data on deny, that`s pretty awesome!
    else:
        # GET : Display the "Add New Task" form
        return render(request, "tasks/add.html", {
            "form": NewTaskForm()
        })

# Helpers
def redirect(path_string):
    return HttpResponseRedirect(reverse(path_string))

