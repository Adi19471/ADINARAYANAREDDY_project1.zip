from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import date
import datetime
today = date.today()

from datetime import datetime


# Create your views here.
def home_view(request):
    now = date.today()
    d1 = today.strftime("%m,%d,%y")

    nows = datetime.now()

    

    d2 = now.strftime("%d,%m,%Y,%H:%M:%S")
    
    print(d2)
    print()
    print(nows)
    print()
    print(now)
    print()
  
    s = {
        "Django":"DEVLOPER ADI",
        'python':"Django"
    }
    return HttpResponse(s)