from django.db import models

# Create your models here.
class Portfolio(models.Model) : 
    name  = models.CharField(max_length=255) # have to use max length for a CharField
    description = models.TextField(blank=False, null=False)
