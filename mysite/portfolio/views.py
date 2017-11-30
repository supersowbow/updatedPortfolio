from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError


# Create your views here.

def index(request):
    #The Home Page for Porfiolio site
    return render(request, 'portfolio/index.html')

def projects(request):
    #The Home Page for Porfiolio site
    return render(request, 'portfolio/projects.html')

def email(request):
    return render(request, 'portfolio/email.html')
