from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Print_Hello(request):
    movie_details={'movies':[
        {
        "Title":"titanic",
        "year":1998,
        "summery":"ship crash",
        "success":True
      },
       {
        "Title":"Persuite of happiness",
        "year":1999,
        "summery":"life cahnges",
        "success":True
      }, {
        "Title":"after fell",
        "year":2009,
        "summery":"love story",
        "success":False
      },
    ]
    }
    return render(request,'index.html',movie_details) 