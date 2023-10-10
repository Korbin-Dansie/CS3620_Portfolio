from django.shortcuts import redirect, render
from portfolio.forms import ContactForm, PortfolioForm
from portfolio.models import Portfolio, Hobby
from django.contrib import messages

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Home",
    }
    return render(request, "home.html", my_context) # return an html template

def portfolio_view(request, *args, **kwargs):
    """ Display all the portfolio items for guests """
    my_context = {
        "site_title": "Portfolio",
        "portfolio_list": Portfolio.objects.all()
    }
    return render(request, "portfolio/portfolio/portfolio.html", my_context) # return an html template

def portfolio_detail_view(request, portfolio_id, *args, **kwargs):
    """ Display a portfolio item in more detail """
    my_context = {
        "site_title": "Portfolio",
        "item": Portfolio.objects.get(pk=portfolio_id),
    }
    return render(request, "portfolio/portfolio/portfolio_detail.html", my_context) # return an html template

def portfolio_manage_view(request, *args, **kwargs):
    """ For admins display a list of portfolio items that can be edited or deleted """
    my_context = {
        "site_title": "Manage Portfolio",
        "portfolio_list": Portfolio.objects.all()
    }
    return render(request, "portfolio/portfolio/portfolio_manage.html", my_context) # return an html template

def portfolio_upsert_view(request, portfolio_id, *args, **kwargs):
    """ Create or edit an existing portfolio item. New items have an id of 0 """
    form = PortfolioForm(request.POST or None)
    try:
        instance = Portfolio.objects.get(pk=portfolio_id)
    except Portfolio.DoesNotExist:
        instance = None

    if request.method == 'POST': # Check if the usersubmited the form correctly then redirect them
        print("Form was posted")
        form = PortfolioForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('portfolio_manage') # Return them to portfolio database home page
    else:
        form = PortfolioForm(instance=instance)

    site_tile = ""
    if (portfolio_id == 0):
        site_tile = "Create Portfolio"
    else:
        site_tile = "Edit Portfolio"
    my_context = {
        "site_title": site_tile,
        "form": form,
    }
    return render(request, "portfolio/portfolio/portfolio_upsert.html", my_context) # return an html template

def portfolio_delete_view(request, portfolio_id, *args, **kwargs):
    """ Create or edit an existing portfolio item. New items have an id of 0 """
    try:
        instance = Portfolio.objects.get(pk=portfolio_id)
        instance.delete()
    except Portfolio.DoesNotExist:
        instance = None
    
    return redirect('portfolio_manage') # Return them to portfolio database home page


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
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Thank you, I will be in touch soon.") # Display a succcessful contact submition
            return redirect("contact") # Return via GET to prevent resubmit
    my_context = {
        "site_title": "Contact",
        "form": form
    }
    return render(request, "contact.html", my_context) # return an html template  
