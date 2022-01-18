from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeView(request):
    return HttpResponse("<h1>Wellcome to OSLP Homepage</h1>")