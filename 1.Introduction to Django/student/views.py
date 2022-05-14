from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello World...")

def henry(request):
    return HttpResponse("My name is Henry")