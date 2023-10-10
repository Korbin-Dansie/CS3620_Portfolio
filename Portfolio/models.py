import datetime
from django.db import models

# Create your models here.
class Portfolio(models.Model) : 
    name  = models.CharField(max_length=255) # have to use max length for a CharField
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="portfolio", null=False, blank=False)
    image_alt = models.CharField(max_length=255, blank=True) # Used for alt text of the image
    def __str__(self):
        return self.name

class Hobby(models.Model) : 
    name  = models.CharField(max_length=255) # have to use max length for a CharField
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="hobby", max_length=255, null=False, blank=False)
    image_alt = models.CharField(max_length=255, blank=True) # Used for alt text of the image
    def __str__(self):
        return self.name
    

class Contact(models.Model) : 
    name  = models.CharField(max_length=255, blank=False, null=False) # have to use max length for a CharField
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(max_length=1024, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " --- " + datetime.datetime.strftime(self.created_at, '%Y-%m-%d')
