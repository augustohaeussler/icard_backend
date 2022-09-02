from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(unique=True, max_length=50, blank=False)
    country = models.CharField(max_length=50, blank=True)
    picture = models.URLField(blank=True)
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']    