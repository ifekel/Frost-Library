from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    profile_img = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    # def get_absolute_url(self):
    #     return reverse('viewname')