from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. I am Shreyas Basutkar. My First Django Project.")
