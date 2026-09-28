from django.shortcuts import render
from django.http import HttpResponse
from hello.forms import login_info

# Create your views here.
def show(req):
    return render(req,'hello/greet.html')

# def sh(req):
#     return render(req,'hello/base.html')

def login(req):
    lg = login_info()
    return render(req,'hello/login.html',{'login' : lg})