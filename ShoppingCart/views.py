import json
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from myapi.models import BookDetails
from django.http import HttpResponse


# Create your views here.
def retrieve(response, userid):
    order = Order.objects.get(id=userid)
    books = []

    for item in order.orderitem_set.all():
        if not item.bought:
            books.append(item.book.ISBN.Title)

    jbooks = json.dumps(books)
    return HttpResponse(jbooks)


def update(response, userid, bookid):
    order = Order.objects.get(id=userid)
    book = BookDetails.objects.get(id=bookid)

    for item in order.orderitem_set.all():
        if item.book == book:
            item.amount = item.amount + 1
            item.save()
            order.save()
            return HttpResponse("Amount of Book increased!")

    order_item = OrderItem.objects.all()
    order_item.create(order=order, book=book, amount=1, bought=False, saved=False)

    return HttpResponse("Book Added!")


def delete_order_item(request, orderitemid, userid):
    order = Order.objects.get(id=userid)
    order_item = OrderItem.objects.get(id=orderitemid)

    if order_item.amount > 1:
        order_item.amount = order_item.amount - 1
        order_item.save()
    else:
        order_item.delete()

    order.save()

    return HttpResponse("1 Book removed!")

    #return redirect('/Order/')