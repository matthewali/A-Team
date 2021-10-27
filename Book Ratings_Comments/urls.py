from django.contrib.auth import logout
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('', views.rateBook, name='rate'),
    path('login/', views.loginPage, name="login"),
    path("books/", views.Booklist.as_view()),
    path("ratings/", views.Ratings.as_view()),
    path("ratings/<int:pk>", views.RatingsDetails.as_view()),
    path("logout", views.logout_request, name="logout"),
]