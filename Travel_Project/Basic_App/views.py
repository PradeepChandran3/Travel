# (Function 1)
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

# (Function 1)
# def base (request):
#     return HttpResponse ("Hello World")

# (Function 2)
# def base (request):
#     return render(request,"basic.html")

# (Function 3)
# def base (request):
#     name="Kerala"
#     return render(request,"basic.html",{'obj':name})

# # (Function 4)
def base (request):
    return render(request,"home.html")
def addition (request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return render(request,"result.html",{'answer':add,'answer1':sub,'answer2':mul,'answer3':div})

