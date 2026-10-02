from django import forms

class stu_registratation(forms.Form):
    Roll_no = forms.IntegerField()
    Name = forms.CharField()
    Age = forms.CharField()
    Email = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)
