from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from myapi.models import BookDetails


# Create your models here.
class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="shoppingcart", null=True)

    def __str__(self):
        return str(self.user.username) + "'s cart"

    # def subtotal(self):
    #     amount = 0.00
    #     for item in self.orderitem_set.all():
    #         if not item.saved and not item.bought:
    #             amount = amount + float(item.quantity * item.book.Price)
    #     return "%.2f" % amount

    def __repr__(self):
        return '<Order object ({}) "{}">'.format(self.id, self.user.username)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(BookDetails, on_delete=models.CASCADE)
    amount = models.IntegerField()
    bought = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return self.book.ISBN.Title

    # def total(self):
    #     return round(self.amount * self.book.Price, 2)
