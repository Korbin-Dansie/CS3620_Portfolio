from django.shortcuts import render
from hobbies.models import Hobby

# Create your views here.
def hobbies_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Hobbies",
        "hobby_list": Hobby.objects.all()
    }
    return render(request, "hobbies.html", my_context) # return an html template