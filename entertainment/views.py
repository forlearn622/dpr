from django.shortcuts import render
from entertainment.forms import ent_form
from django.http import HttpResponseRedirect

# Create your views here.
def type_ent(req):
    if req.method == 'POST':
        fm = ent_form(req.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            return HttpResponseRedirect('/entertainment/ent_suc')
    else:
        fm = ent_form()
    return render(req,'entertainment/myform.html',{'form' : fm})

def ent_suc(req):
    return render(req,'entertainment/reg_done.html')