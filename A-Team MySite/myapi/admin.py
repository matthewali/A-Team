from django.contrib import admin
from .models import BookDetails, BookRating, Order, OrderItem
from .models import Book
from .models import Genre
from .models import Publisher
from .models import Author
admin.site.register(BookDetails)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(BookRating)
admin.site.register(Order)
admin.site.register(OrderItem)

