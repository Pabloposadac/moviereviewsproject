from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return render(request, 'home.html')
    #return HttpResponse('<h1> Welcome to Home Page</h1>')
    return render(request, 'home.html',{'name':'Pablo Posada Colorado'})

def about(request):
    return render(request, 'about.html')