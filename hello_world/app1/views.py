from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request,'a.html',{'title':'vrushali'})

def profile(request):
    return HttpResponse("profile page")

def address(request):
    return HttpResponse("adress page")

def expression(request):
    a=int(request.GET['text1'])
    b=int(request.GET['text2'])
    c=a+b
    return render(request,'exp.html',{'result':c})