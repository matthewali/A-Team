import json

from django.shortcuts import render, redirect
from .models import Order, OrderItem
from django.http import HttpResponse


# Create your views here.
def retrieve(response, userid):
    # userid = response.user.id
    order = Order.objects.get(id=userid)
    books = []

    for item in order.orderitem_set.all():
        if not item.bought:
            books.append(item.book.ISBN.Title)

    jbooks = json.dumps(books)
    return HttpResponse(jbooks)


def delete_order_item(request, orderitemid, userid):
    #     userid = request.user.id
    order = Order.objects.get(id=userid)
    orderitem = OrderItem.objects.get(id=orderitemid)

    if request.method == "POST":
        orderitem.delete()
        order.save()
        return redirect('/Order/')


#
#
# def save_for_later(request, cartitemid):
#     userid = request.user.id
#     cart = ShoppingCart.objects.get(id=userid)
#     cartitem = ShoppingCartItem.objects.get(id=cartitemid)
#
#     if request.method == "POST":
#         cartitem.savedforlater = True
#         cartitem.save()
#
#     cart.save()
#
#     return redirect('/ShoppingCart/')
#
#
# def move_to_cart(request, cartitemid):
#     userid = request.user.id
#     cart = ShoppingCart.objects.get(id=userid)
#     cartitem = ShoppingCartItem.objects.get(id=cartitemid)
#
#     if request.method == "POST":
#         cartitem.savedforlater = False
#         cartitem.save()
#
#     cart.save()
#
#     return redirect('/ShoppingCart/')
#
#
# def update_quantity(request, cartitemid):
#     userid = request.user.id
#     cart = ShoppingCart.objects.get(id=userid)
#     cartitem = ShoppingCartItem.objects.get(id=cartitemid)
#
#     if request.method == "POST":
#         newquantity = request.POST['UpdateValue']
#         if int(newquantity) <= 0:
#             raise Exception("new quantity must be greater than 0")
#         cartitem.quantity = newquantity
#         cartitem.save()
#         cart.save()
#
#     return redirect('/ShoppingCart/')
#
#
# def checkout(request):
#     userid = request.user.id
#     cart = ShoppingCart.objects.get(id=userid)
#
#     if request.method == "POST":
#         for item in cart.shoppingcartitem_set.all():
#             if not item.savedforlater:
#                 item.ordered = True
#                 item.save()
#                 cart.save()
#
#     return redirect('/ShoppingCart/')
