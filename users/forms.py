from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Can change the users here 
class RegistrationForm(UserCreationForm):
    email = forms.EmailField() # add email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"] # What variable do we want the from to display