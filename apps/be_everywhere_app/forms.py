from django import forms
from .models import Users

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length = 100, widget=forms.PasswordInput())
    class Meta:
        model = Users
        fields = ['first', 'last', 'email', 'password'] + ['confirm_password']
        widgets = {'password':forms.PasswordInput(),}
