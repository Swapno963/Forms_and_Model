from django.shortcuts import render
from . import forms
# Create your views here.


def Show_form(request):
    form = forms.ExampleForm()
    return render(request, 'django_forms.html',{'form':form})