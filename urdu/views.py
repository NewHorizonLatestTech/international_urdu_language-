from django.http import HttpResponse
from django.shortcuts import render
from . import views


# Create your views here.

def home(request):
    return render(request, 'urdu/home.html')


def index(request):
    return render(request, 'urdu/index.html')
