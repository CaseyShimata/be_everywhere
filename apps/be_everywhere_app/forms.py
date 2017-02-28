from django import forms
from .models import Users

class RegisterForm(forms.ModelForm):
    pass_conf = forms.CharField(max_length = 100, widgets=forms.PasswordInput)
    class Meta:
        model = Users
        fields = ['first', 'last', 'email', 'password'] + ['pass_conf']
        widgets = {'password':forms.PasswordInput()}
