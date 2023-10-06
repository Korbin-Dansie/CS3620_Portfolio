from django.shortcuts import render
from portfolio.models import Portfolio, Hobby

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Home",
    }
    return render(request, "home.html", my_context) # return an html template

def portfolio_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Portfolio",
        "portfolio_list": Portfolio.objects.all()
    }
    return render(request, "portfolio/portfolio/portfolio.html", my_context) # return an html template

def portfolio_detail_view(request, portfolio_id, *args, **kwargs):
    my_context = {
        "site_title": "Portfolio",
        "item": Portfolio.objects.get(pk=portfolio_id),
    }
    return render(request, "portfolio/portfolio/portfolio_detail.html", my_context) # return an html template

def hobbies_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Hobbies",
        "hobby_list": Hobby.objects.all()
    }
    return render(request, "portfolio/hobby/hobbies.html", my_context) # return an html template

def hobbies_detail_view(request, hobby_id, *args, **kwargs):
    my_context = {
        "site_title": "Hobbies",
        "item": Hobby.objects.get(pk=hobby_id),
    }
    return render(request, "portfolio/hobby/hobbies_detail.html", my_context) # return an html template

def contact_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Contact",
    }
    return render(request, "contact.html", my_context) # return an html template

    
