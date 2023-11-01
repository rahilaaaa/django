from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Print_Hello(request):
    movie_details={
        "Title":"titanic",
        "year":1998,
        "summery":"ship crash",
        "success":True
    }
    return render(request,'index.html',movie_details)
        
        
    
