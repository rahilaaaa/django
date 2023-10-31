from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Print_Hello(request):
    return HttpResponse("Hello World")
        
    
