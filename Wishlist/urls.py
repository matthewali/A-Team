from django.contrib.auth import logout
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path("books/", views.Booklist.as_view()),
    path("logout", views.logout_request, name="logout"),
    path("index/", views.indexPage, name='index'),
    path('Wishlist/', views.Booklist.as_view()),
    
]