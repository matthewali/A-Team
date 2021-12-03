from rest_framework import serializers
from .models import *

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Wishlist
        fields=["title"]

    