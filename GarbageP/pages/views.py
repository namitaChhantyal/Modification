from django.shortcuts import render
from django.http import HttpResponse
from .models import Page

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse('about')