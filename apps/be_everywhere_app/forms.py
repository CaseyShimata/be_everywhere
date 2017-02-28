from django import forms
from .models import Users

class RegisterForm(forms.ModelForm):
    confirm_assword = forms.CharField(max_length = 100, widget=forms.PasswordInput())
    class Meta:
        model = Users
        fields = ['first', 'last', 'email', 'password'] + ['confirm_assword']
        widgets = {'password':forms.PasswordInput(),}

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']
        widgets = {'password':forms.PasswordInput(),}

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']
        widgets = {'password':forms.PasswordInput(),}
