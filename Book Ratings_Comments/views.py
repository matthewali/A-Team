from .forms import CreateUserForm
from .forms import CreateRatingForm
from .models import Book, BookRating
from .serializers import BookSerializer, RatingSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models.signals import post_save
from rest_framework import generics, response
from typing import ContextManager
# Create your views here.
class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Ratings(generics.ListCreateAPIView):
    queryset = BookRating.objects.all()
    serializer_class = RatingSerializer

class RatingsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookRating.objects.all()
    serializer_class = RatingSerializer

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)

    context = {'form':form}
    return render(request, 'bookstore/register.html', context)

def loginPage(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('rate')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")
    context = {'form': form}
    return render(request, 'registration/login.html', context)

def rateBook(request):
    form = CreateRatingForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.reviewer = request.user
        review.save()
        form = CreateRatingForm()

    context = {'form': form}
    return render(request, 'bookstore/bookratings.html', context)

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")