from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request, *args, **kwargs):
    form = UserCreationForm()
    my_context = {
        "site_title": "Home",
        'form': form,
    }
    return render(request, "users/register.html", my_context)