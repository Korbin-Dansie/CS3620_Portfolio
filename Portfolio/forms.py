from django import forms
from portfolio.models import Hobby, Portfolio, Contact

# Can change the users here 
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                'placeholder': 'Name'
                }),
            "email": forms.TextInput(attrs={
                "class": "form-control",
                'placeholder': 'Email'
                }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                'placeholder': 'Message'
                }),
        }


