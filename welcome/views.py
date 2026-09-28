from django.shortcuts import render

# Create your views here.
def eng_greet(req):
    return render(req,'welcome/eng.html')

def usa_greet(req):
    return render(req,'welcome/usa.html')

def series(req):
    return render(req,'welcome/series.html')
