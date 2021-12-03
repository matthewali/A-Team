from django.db.models.aggregates import Avg
from django.db.models.query import QuerySet
from django.utils.html import avoid_wrapping
from .forms import CreateUserForm, CreateRatingForm
from .models import Book, BookRating
from .serializers import BookSerializer, RatingSerializer, StatSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.signals import post_save
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, response
from rest_framework.parsers import JSONParser
from typing import ContextManager
from bookstore import serializers

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

class BookStats(generics.ListCreateAPIView):
    queryset = BookRating.objects.all().order_by('-num_stars')
    serializer_class = StatSerializer

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            success_message = 'Thank you for registering! Please log in to access site.'
            return redirect('index')

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

def indexPage(request):
    return render(request, 'bookstore/index.html')

@csrf_exempt
def user_review(request):
    if request.method == "GET":
        reviews = BookRating.objects.all()
        serializer = RatingSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = RatingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def review_detail(request, pk):
    try:
        review = BookRating.objects.get(pk=pk)
    except BookRating.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = RatingSerializer(review)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = RatingSerializer(review, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        review.delete()
        return HttpResponse(status=204)