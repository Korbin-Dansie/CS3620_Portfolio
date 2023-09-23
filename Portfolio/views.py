from django.shortcuts import render
from portfolio.models import Portfolio

# Create your views here.
def portfolio_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Portfolio",
        "portfolio_list": Portfolio.objects.all()
    }
    return render(request, "portfolio.html", my_context) # return an html template