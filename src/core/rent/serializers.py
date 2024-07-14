from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class RentSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.Rent
        fields = ('user', 'product', 'startDate', 'endDate')

    def create(self, validated_data):
        """Create and return a new user."""

        rent = models.Rent(
                user = validated_data['user'],
                product = validated_data['product'],
                startDate = validated_data['startDate'],
                endDate = validated_data['endDate'],
        )

        rent.save()

        return rent