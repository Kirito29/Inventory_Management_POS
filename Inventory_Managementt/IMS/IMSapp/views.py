from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(response):
    return HttpResponse("This is the index page")

def page2(response):
    return HttpResponse("This is the second page")
