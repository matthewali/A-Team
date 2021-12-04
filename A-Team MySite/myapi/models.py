from django.db import models
from django.urls import reverse
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.db.models.base import Model

class Book(models.Model):
    ISBN = models.CharField(max_length=60)
    Title = models.CharField(max_length=60)
    Description = models.CharField(max_length=60)
    PublishDate = models.DateField()

    def __str__(self):
        return self.Title


class Genre(models.Model):
    GenreID = models.CharField(max_length=60)
    Type = models.CharField(max_length=60)

    def __str__(self):
        return self.Type


class Publisher(models.Model):
    PublisherID = models.CharField(max_length=60)
    Name = models.CharField(max_length=60)

    def __str__(self):
        return self.Name


class Author(models.Model):
    AuthorID = models.CharField(max_length=60)
    FName = models.CharField(max_length=60)
    LName = models.CharField(max_length=60)
    Biography = models.CharField(max_length=60)

    class Meta:
        ordering = ['LName', 'FName']

    def get_absolute_url(self):

        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.LName, self.FName)


class BookDetails(models.Model):
    ID = models.CharField(max_length=60)
    Price = models.CharField(max_length=60)
    CopiesSold = models.CharField(max_length=60)
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
    GenreID = models.ForeignKey(Genre, on_delete=models.CASCADE)
    PublisherID = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    AuthorID = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['ISBN', 'AuthorID']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)

    def createprofile(sender, instance, created, **kwargs):

        if created:
            userid = instance.id
            Profile.objects.create(user=instance, id=userid)
            Order.objects.create(user=instance, id=userid)

            print('Profile and Order Created!')

    post_save.connect(createprofile, sender=User)


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="shoppingcart", null=True)

    def __str__(self):
        return str(self.user.username) + "'s cart"

    def __repr__(self):
        return '<Order object ({}) "{}">'.format(self.id, self.user.username)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.IntegerField()
    bought = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return self.book.ISBN.Title

    def display_genre(self):
        return ', '.join([genre.type for genre in (self.genre, all()[:3])])

    display_genre.short_description = 'Genre'


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

class Wishlist(models.Model):
    title = models.CharField(max_length=255, blank= True, null=True)
    author = models.CharField(max_length=255, blank= True, null=True)
    
    def __str__(self):
       return self.title    
