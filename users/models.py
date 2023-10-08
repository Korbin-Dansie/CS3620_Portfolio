from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create a custom profile to go with the user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Change were images are stored in setting.py (add base directories)
    image = models.ImageField(default='blank-user-profile.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username