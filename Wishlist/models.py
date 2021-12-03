from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Wishlist(models.Model):
    title = models.CharField(max_length=255, blank= True, null=True)
    author = models.CharField(max_length=255, blank= True, null=True)
    
    def __str__(self):
       return self.title
