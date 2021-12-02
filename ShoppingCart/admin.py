from django.contrib import admin
from .models import Order, OrderItem, Profile

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
