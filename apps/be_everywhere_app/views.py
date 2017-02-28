from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import RegisterForm, LoginForm
from models import Users

# Create your views here.
def homepage(request):
    return render(request, 'be_everywhere_app/homepage.html')

def log_reg(request):
    regform = RegisterForm()
    logform = LoginForm()
    context = {'regform':regform, 'logform':logform}
    return render(request, 'be_everywhere_app/login_registration.html', context)

def about(request):
    return render(request, 'be_everywhere_app/about.html')

def register(request):
    if request.method == "POST":
        user = Users.objects.regvalidation(request.POST)
        if 'errors' in user:
            for error in user['errors']:
                messages.error(request, error)
                return redirect('/register')
        else:
            request.session['logged'] = {
               'email': user['theuser'].email,
               'id': user['theuser'].id,
               'first': user['theuser'].first,
               'last': user['theuser'].last,
               'permission': user['theuser'].permission
           }
    return redirect('/')
