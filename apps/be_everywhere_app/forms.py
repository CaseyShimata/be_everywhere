from django import forms
from .models import Users, Events


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length = 100, widget=forms.PasswordInput())
    class Meta:
        model = Users
        fields = ['first', 'last', 'email', 'password'] + ['confirm_password']
        widgets = {'password':forms.PasswordInput(),}

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']
        widgets = {'password':forms.PasswordInput(),}

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'location', 'description', 'rate', 'image']
