from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=500, default='')
    state = models.CharField(max_length=500, default='')
    city = models.CharField(max_length=100, default='')
    country = models.TextField(max_length=255, default='')
    zipcode = models.CharField(max_length=100, default='')
    
    def __str__(self):
        return self.username
    
    # def get_absolute_url(self):
    #     return reverse('viewname')