from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.Products
        fields = ('brand', 'model', 'category', 'weight', 'height', 'altitude', 'endurance', 'wingspan', 'payload',)

    def create(self, validated_data):
        """Create and return a new user."""

        product = models.Products(
                brand = validated_data['brand'],
                model = validated_data['model'],
                category = validated_data['category'],
                weight = validated_data['weight'],
                height = validated_data['height'],
                altitude = validated_data['altitude'],
                endurance = validated_data['endurance'],
                wingspan = validated_data['wingspan'],
                payload = validated_data['payload']
        )

        product.save()

        return product
