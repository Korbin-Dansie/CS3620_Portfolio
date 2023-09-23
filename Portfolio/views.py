from django.shortcuts import render

# Create your views here.
def portfolio_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Portfolio",
    }
    return render(request, "portfolio.html", my_context) # return an html template