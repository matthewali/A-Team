from django.urls import path
from shoppingcart import views

urlpatterns = [
    path("delete/<int:userid>/<int:orderitemid>", views.delete_order_item, name="deleteorderitem"),
    path("retrieve/<int:userid>", views.retrieve, name="retrieve"),
    # path("update/<int:orderitemid>", views.update, name="update"),
]