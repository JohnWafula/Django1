from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to emobilis")


def about(request):
    return HttpResponse("About emobilis")
