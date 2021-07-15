from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.SlugRelatedField(read_only=True, slug_field='title')
    commenter = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = Comment
        fields = [
            'pk',
            'article',
            'commenter',
            'image',
            'body',
            'date',
        ]

