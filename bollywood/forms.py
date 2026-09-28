from django import forms

class register_info(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.IntegerField()
    city = forms.CharField()
    
