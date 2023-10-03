from django.shortcuts import render
from portfolio.models import Portfolio, Hobby

# Create your views here.
def portfolio_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Portfolio",
        "portfolio_list": Portfolio.objects.all()
    }
    return render(request, "portfolio.html", my_context) # return an html template


def home_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Home",
    }
    return render(request, "home.html", my_context) # return an html template


def hobbies_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Hobbies",
        "hobby_list": Hobby.objects.all()
    }
    return render(request, "hobbies.html", my_context) # return an html template


def contact_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Contact",
    }
    return render(request, "contact.html", my_context) # return an html template