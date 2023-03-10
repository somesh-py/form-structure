from django.shortcuts import render
from .forms import Userregistration
# Create your views here.

def form(request):
    fm=Userregistration(auto_id=True,label_suffix=' ',initial={'name':'som','contact':'8818808249','email':'somesh615@gmail.com','address':'dhar','password':'enter password'})
    fm.order_fields(field_order=[])
    return render(request,'forms/index.html',{'forms':fm})