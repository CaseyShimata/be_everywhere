from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'be_everywhere_app/homepage.html')

def log_reg(request):
    return render(request, 'be_everywhere_app/log_reg.html')

def about(request):
    return render(request, 'be_everywhere_app/about.html')
