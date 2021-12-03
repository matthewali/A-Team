from django.contrib.auth.models import User
from django.db.models.aggregates import Avg, Count
from django.db.models.expressions import OrderBy
from rest_framework import serializers
from .models import Book, BookRating

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title"]

class RatingSerializer(serializers.ModelSerializer):
    bookTitle = serializers.CharField(source='book.title')
    class Meta:
        model = BookRating
        fields = [
            "bookTitle",
            "pk",
            "title",
            "book",
            "num_stars",
            "comment",
            "review_date",
            "reviewer",    
        ]
class StatSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='book.title')
    averageRating = serializers.SerializerMethodField()
    class Meta:
        model = BookRating
        fields = [
           'title',
           'num_stars',
           'comment',
           'review_date',
           'averageRating',
        ]
    def get_averageRating(self, obj):
        return BookRating.objects.aggregate(average_rating=Avg('num_stars'))
    