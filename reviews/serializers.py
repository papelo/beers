from rest_framework import serializers
from reviews.models import Review
from beers.models import Beer
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    beer = serializers.PrimaryKeyRelatedField(queryset=Beer.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'rev_text', 'rev_puntuation', 'owner', 'beer']


class UserSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'reviews']

