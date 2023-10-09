from django import forms
from portfolio.models import Hobby, Portfolio

# Can change the users here 
class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = "__all__"


