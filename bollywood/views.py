from django.shortcuts import render
from bollywood.forms import register_info
# Create your views here.

def bolly(req):
    return render(req,'bollywood/bolly.html')

def register(req):
    rg = register_info()
    return render(req,'bollywood/bollyform.html',{'register': rg})
