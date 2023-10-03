from django.contrib import admin

# Register your models here.
from .models import Portfolio
admin.site.register(Portfolio)

from .models import Hobby
admin.site.register(Hobby)