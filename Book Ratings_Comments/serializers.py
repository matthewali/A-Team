from rest_framework import serializers
from .models import Book, BookRating

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title"]

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRating
        fields = [
            "pk",
            "title",
            "book",
            "num_stars",
            "comment",
            "review_date",
            "reviewer"
        ]