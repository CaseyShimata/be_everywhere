from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'be_everywhere_app/homepage.html')
