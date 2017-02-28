from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import RegisterForm

# Create your views here.
def homepage(request):
    return render(request, 'be_everywhere_app/homepage.html')

def log_reg(request):
    form = RegisterForm()
    context = {'regform':form}
    return render(request, 'be_everywhere_app/log_reg.html', context)

def about(request):
    return render(request, 'be_everywhere_app/about.html')
