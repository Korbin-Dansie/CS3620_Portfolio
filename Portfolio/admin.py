from django.contrib import admin

# Register your models here.
from .models import Portfolio
admin.site.register(Portfolio)

from .models import Hobby
admin.site.register(Hobby)


# Because date is readonly it is more coplicated to display in admin dashboard
from .models import Contact
admin.site.register(Contact)
