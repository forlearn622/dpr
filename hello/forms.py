from django import forms

class login_info(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()