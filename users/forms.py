from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField

# Can change the users here 
class RegistrationForm(UserCreationForm):
    email = forms.EmailField() # add email
    # username = forms.CharField(max_length=150)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"] # What variable do we want the from to display


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }
))

