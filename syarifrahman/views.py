from django.shortcuts import render
from django.contrib import admin

from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'about/index.html')
