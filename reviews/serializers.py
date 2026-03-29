from rest_framework import serializers
from reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # shows username
    class Meta:
        model = Review
        fields = ['id', 'gun', 'user', 'text', 'rating', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']


