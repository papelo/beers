from rest_framework import serializers
from beers.models import Beer
from reviews.models import Review
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rev_text', 'rev_puntuation']


class BeerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Beer
        fields = ['id', 'name', 'graduation', 'owner', 'reviews']


class UserSerializer(serializers.ModelSerializer):
    beers = serializers.PrimaryKeyRelatedField(many=True, queryset=Beer.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'beers']

