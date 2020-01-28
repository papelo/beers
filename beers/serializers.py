from rest_framework import serializers
from beers.models import Beer
from django.contrib.auth.models import User


class BeerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Beer
        fields = ['id', 'name', 'graduation', 'owner']

class UserSerializer(serializers.ModelSerializer):
    beers = serializers.PrimaryKeyRelatedField(many=True, queryset=Beer.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'beers']

