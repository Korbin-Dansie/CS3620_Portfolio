from django.db import models

# Create your models here.
class Portfolio(models.Model) : 
    name  = models.CharField(max_length=255) # have to use max length for a CharField
    description = models.TextField(blank=False, null=False)
    image = models.CharField(max_length=255, null=True, blank=True)
    image_alt = models.CharField(max_length=255, blank=True) # Used for alt text of the image
    def __str__(self):
        return self.name

class Hobby(models.Model) : 
    name  = models.CharField(max_length=255) # have to use max length for a CharField
    description = models.TextField(blank=False, null=False)
    image = models.CharField(max_length=255, null=True, blank=True)
    image_alt = models.CharField(max_length=255, blank=True) # Used for alt text of the image
    def __str__(self):
        return self.name
