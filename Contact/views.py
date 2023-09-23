from django.shortcuts import render

# Create your views here.
def contact_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Contact",
    }
    return render(request, "contact.html", my_context) # return an html template