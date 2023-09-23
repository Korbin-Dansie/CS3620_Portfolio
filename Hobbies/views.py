from django.shortcuts import render

# Create your views here.
def hobbies_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Hobbies",
    }
    return render(request, "hobbies.html", my_context) # return an html template