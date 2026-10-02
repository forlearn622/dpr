from django.shortcuts import render
from PostMethod.forms import stu_registratation
from django.http import HttpResponseRedirect

# Create your views here.

def stu_reg(req):
    if req.method == 'POST':
        form = stu_registratation(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/PostMethod/suc')
    else:
        form = stu_registratation()
    return render(req,'PostMethod/RegistrationForm.html',{'form' : form})

def reg_suc(req):
    return render(req,'PostMethod/Success.html')
