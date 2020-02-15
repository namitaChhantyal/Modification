from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# from .models import Page
# from allauth.account.views import LoginView

# class MyLogInView(LoginView):
#     template_name='Templates/login.html'

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')

def payment(request):
    # pages=Page.object.all()
    # context=[
    #     'pages':pages
    # ]
    return render(request,'payment.html')

# def accounts(request):
#     return render(request,'about.html')

# def login(request):
#     if request.method == 'POST':
#         # username = request.POST.get('')
#         # password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#          return render(request, 'payment.html', {})