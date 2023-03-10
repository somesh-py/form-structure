from django.shortcuts import render
from .forms import Studentregistration
# Create your views here.


def index(request):
    fm=Studentregistration()
    return render(request,'index.html',{'forms':fm})