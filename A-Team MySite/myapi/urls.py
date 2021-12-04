#myapi/urls.py

from django.urls import path
from . import views
from django.urls.resolvers import URLPattern
from django.contrib.auth import logout
from myapi import views

urlpatterns = [
    path('', views.index, name='index'), 
    #path('books/', views.BookListView.as_view(), name='books'),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>', views.BookDetails.as_view()),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
         views.AuthorDetailView.as_view(), name='author-detail'), 
    path('register/', views.registerPage, name="register"),
    path('', views.rateBook, name='rate'),
    path('login/', views.loginPage, name="login"),
    path("books/", views.Booklist.as_view()),
    path("stats/", views.BookStats.as_view()),
    path("ratings/", views.Ratings.as_view()),
    path("ratings/<int:pk>", views.RatingsDetails.as_view()),
    path("logout", views.logout_request, name="logout"),
    path("index/", views.indexPage, name='index'),
    path('reviews/', views.user_review),
    path('reviews/<int:pk>/', views.review_detail),
    path("delete/<int:userid>/<int:orderitemid>", views.delete_order_item, name="deleteorderitem"),
    path("retrieve/<int:userid>", views.retrieve, name="retrieve"),
    path("update/<int:userid>/<int:bookid>", views.update, name="update"),
    path('Wishlist/', views.Booklist.as_view()),
]

