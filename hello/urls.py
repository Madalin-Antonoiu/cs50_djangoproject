from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
     path("<str:name>", views.greet, name="greet"), # We execute views.greet function whenever we type/hello/ "any name"
    path("mads", views.mads, name="mads")
]