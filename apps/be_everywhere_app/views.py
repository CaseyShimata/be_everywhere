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

def admin_manage_users(request):
    if ['logged'].permission = 2 #assuming basic users are 1, admin are 3 and vendors 1?
        context = {
            ['logged'].id: id,
            'users': Users.objects.all()
        }
        return render(request, "be_everywhere_app/admin_manage_users", context)
    else
        redirect('be_everywhere_app/homepage.html')

def user_manage_events(request):
    context = {
        ['logged'].id: id,
        'my_events': Events.objects.filter(event_order.user=id)
    }
        return render(request, "be_everywhere_app/admin_manage_events", context)

def admin_manage_products(request):
    return render(request, 'be_everywhere_app/admin_manage_products.html')

def admin_product_sales(request):
    return render(request, 'be_everywhere_app/admin_product_sales.html')

def attendees_become_an_operator(request):
    return render(request, 'be_everywhere_app/attendees_become_an_operator.html')

def my_messages(request):
    return render(request, 'be_everywhere_app/my_messages.html')

def view_event(request):
    return render(request, 'be_everywhere_app/view_event.html')

def view_user(request):
    return render(request, 'be_everywhere_app/view_user.html')

def welcome_admin(request):
    return render(request, 'be_everywhere_app/welcome_admin.html')

def welcome_attendee(request):
    return render(request, 'be_everywhere_app/welcome_attendee.html')
