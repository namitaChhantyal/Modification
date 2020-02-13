from django.shortcuts import render
from django.http import HttpResponse
from .models import Page

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')

def payment(request):
    return render(request,'payment.html')