from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST': # Check if the usersubmited the form correctly then redirect them
        if form.is_valid():
            username = form.cleaned_data.get('username') # Get the username to display it back to the users
            messages.success(request, f"Hello, {username}!\nYour account has been created.")
            return redirect('home') # Return them to portfolio database home page
    
    my_context = {
       "site_title": "Register",
        'form': form
    }
    return render(request, "users/register.html", my_context)