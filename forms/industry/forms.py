from django import forms


class Studentregistration(forms.Form):
    name=forms.CharField(label='your name',label_suffix=' ',required=True,disabled=True,help_text='last limit is 20')
    section=forms.CharField(widget=forms.TextInput(attrs={'class':'section','id':'section'}))
    contact=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'contact','id':'contact'}))
    email=forms.EmailField(label='enter your email',label_suffix=' ',required=True,disabled=False,widget=forms.EmailInput(attrs={'class':'email','id':'email'}))
    school=forms.CharField(label='enter your school name',label_suffix=' ',required=True,disabled=False,widget=forms.TextInput(attrs={'class':'school','id':'school'}))
    address=forms.CharField(label='enter your address',label_suffix=' ',required=False,disabled=False,widget=forms.TextInput(attrs={'class':'address','id':'address'}))