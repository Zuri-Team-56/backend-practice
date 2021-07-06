from .models import Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    school_name = serializers.ReadOnlyField(source='school.name')
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Review
        fields = ['id', 'review', 'rating', 'image', 'author_name', 'school_name', 'educational_status', 'date' ]