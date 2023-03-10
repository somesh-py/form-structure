from django import forms


class Userregistration(forms.Form):
    name=forms.CharField()
    contact=forms.IntegerField()
    email=forms.EmailField()
    address=forms.CharField()
    password=forms.CharField()