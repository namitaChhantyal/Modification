from django.urls import path
from . import views
from django.http import HttpResponseRedirect

urlpatterns=[
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('payment',views.payment,name='payment')
]