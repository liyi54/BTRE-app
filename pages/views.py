from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse('<h1>Hello World!</h1>') # Here's a test. Typically, we would like to render a template instead
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')
# Create your views here.
