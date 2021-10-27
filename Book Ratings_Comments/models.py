from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class BookRating(models.Model):
    title = models.CharField(max_length=255, blank= True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    num_stars = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    review_date = models.DateField(auto_now_add=True)
    #last_modified = models.DateField(auto_now=True)
    reviewer = models.ForeignKey(User,default=None, on_delete=CASCADE)
    
    def __str__(self):
        return self.reviewer.username




