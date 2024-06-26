from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.forms import RegistrationForm # My custom registration form

# Create your views here.
def register_view(request, *args, **kwargs):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST': # Check if the usersubmited the form correctly then redirect them
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username') # Get the username to display it back to the users
            # messages.success(request, f"Hello, {username}!\nYour account has been created.")
            return redirect('users:login') # Return them to portfolio database home page
    
    my_context = {
       "site_title": "Register",
        'form': form
    }
    return render(request, "users/register.html", my_context)

@login_required
def profile_view(request, *args, **kwargs):    
    my_context = {
       "site_title": "Profile",
    }
    return render(request, "users/profile.html", my_context)