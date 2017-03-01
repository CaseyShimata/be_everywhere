from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .forms import RegisterForm, LoginForm, EventForm
from models import Users, Genres

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
            return redirect('/log_reg')
        else:
            request.session['logged'] = {
               'email': user['theuser'].email,
               'id': user['theuser'].id,
               'first': user['theuser'].first,
               'last': user['theuser'].last,
               'permission': user['theuser'].permission
           }
    print request.session['logged']
    return redirect('/')

def login(request):
    if request.method == "POST":
        user = Users.objects.loginvalidation(request.POST)
        if 'errors' in user:
            for error in user['errors']:
                messages.error(request, error)
            return redirect('/log_reg')
        else:
            request.session['logged'] = {
               'email': user['theuser'].email,
               'id': user['theuser'].id,
               'first': user['theuser'].first,
               'last': user['theuser'].last,
               'permission': user['theuser'].permission
           }
        if request.session['logged']['permission'] == 1:
            return redirect('/welcome_admin')
        else:
            return redirect('/')
#alex code
def admin_manage_users(request):
    if ['logged'].permission == 3: #assuming basic users are 1, admin are 3 and vendors 1?
        context = {
            ['logged'].id: id,
            'users': Users.objects.all()
        }
        return render(request, "be_everywhere_app/admin_manage_users.html", context)
    else:
        redirect('be_everywhere_app/homepage.html')

# def attendee_manage_events(request):
#     context = {
#         ['logged'].id: id,
#         'my_events': Events.objects.filter(event_order.user=id)
#     }
    return render(request, "be_everywhere_app/admin_manage_events.html", context)





# all bellow are page rendering methods

def admin_manage_events(request):
    return render(request, 'be_everywhere_app/admin_manage_events.html')

def admin_manage_my_account(request):
    return render(request, 'be_everywhere_app/admin_manage_my_account.html')

def admin_manage_events(request):
    eventform = EventForm()
    context = {'eventform':eventform,
    'genre':Genres.objects.all()}
    return render(request, 'be_everywhere_app/admin_manage_events.html', context)

def admin_manage_products(request):
    return render(request, 'be_everywhere_app/admin_manage_products.html')

def admin_manage_events(request):
    if ['logged'].permission == 3: #assuming basic users are 1, admin are 3 and vendors 1?
        context = {
            'all_events': Events.objects.all()
        }
        return render(request, 'be_everywhere_app/welcome_admin.html')
    else
        return redirect ('/homepage')

def admin_product_sales(request):
    return render(request, 'be_everywhere_app/admin_product_sales.html')

<<<<<<< HEAD
def attendees_manage_my_account(request):
    return render(request, 'be_everywhere_app/attendees_manage_my_account.html')
=======
def attendee_manage_events(request):
    context = {
        ['logged'].id: id,
        'my_events': Events.objects.filter(=id),
        'all_events': Events.objects.all()
    }
    return render(request, 'be_everywhere_app/attendee_manage_events.html', context)
>>>>>>> a2f413581dc0f771eff440e005bef4a394aedc0b

def attendees_become_an_operator(request):
    return render(request, 'be_everywhere_app/attendees_become_an_operator.html')

def attendees_manage_events(request):
    return render(request, 'be_everywhere_app/attendees_manage_events.html')

def my_messages(request):
    return render(request, 'be_everywhere_app/my_messages.html')

def shopping_cart(request):
    return render(request, 'be_everywhere_app/shopping_cart.html')

def view_event(request):
    return render(request, 'be_everywhere_app/view_event.html')

def view_product(request):
    return render(request, 'be_everywhere_app/view_product.html')

def view_user(request):
    return render(request, 'be_everywhere_app/view_user.html')

def welcome_admin(request):
    if ['logged'].permission == 3: #assuming basic users are 1, admin are 3 and vendors 1?
        return render(request, 'be_everywhere_app/welcome_admin.html')
    else
        return redirect ('/homepage')

def welcome_attendee(request):
<<<<<<< HEAD
    return render(request, 'be_everywhere_app/welcome_attendee.html')

# def create_event(request):
    # Events.objects.new(request.POST)
=======
    if ['logged'].permission == 1:
        return render(request, 'be_everywhere_app/welcome_attendee.html')
    else
        return redirect ('/homepage')
>>>>>>> b6c644b2d72204ff91b82c5eba202b1914d8c9ff
