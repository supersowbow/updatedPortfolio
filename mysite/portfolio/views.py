from django.shortcuts import render

# Create your views here.

def index(request):
    #The Home Page for Porfiolio site
    return render(request, 'portfolio/index.html')

def projects(request):
    #The Home Page for Porfiolio site
    return render(request, 'portfolio/projects.html')
