"""
URL configuration for PortfolioDatabase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from portfolio.models import Hobby, Portfolio

from portfolio.views import portfolio_view, portfolio_detail_view, contact_view, hobbies_view, home_view, hobbies_detail_view
urlpatterns = [
    path('', home_view, name='home'), # Change the index page
    path('contact/', contact_view, name='contact'),


    path('hobbies/', hobbies_view, name='hobbies'),
    # hobbies/:id
    path('hobbies/<int:hobby_id>/', hobbies_detail_view, name='hobbies_detail'),


    path('portfolio/', portfolio_view, name='portfolio'),
    path('portfolio/<int:portfolio_id>/', portfolio_detail_view, name='portfolio_detail'),


    path('admin/', admin.site.urls),
]
